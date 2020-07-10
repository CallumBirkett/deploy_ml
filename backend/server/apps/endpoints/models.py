from django.db import models

# Create your models here.


class Endpoint(models.Model):
    '''
    The endpoint object represents a ML API endpoint.

    Attributes:
        name: Name of endpoint used in API URL.
        owner: The string with owner name.
        created_at: The date the endpoint was created.
    '''

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    '''
    Represents the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: Description of the algorithm.
        code: Code that implements the algorithm.
        version: Software version.
        owner: Name of the owner.
        created_at: The date created.
        parent_endpoint: Reference to the endpoint.
    '''

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
    Represents the state of the algorithm which changes with time.

    Attributes:
        status: Status of algorithm in the endpoint. Can be testing, stagin, production, ab_testing.
        active: Boolean flag on the status.
        created_by: Name of creator.
        created_at: Date of status creation.
        parent_mlalgortihm: Corresponding ML algorithm.
    '''

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE, related_name='status')


class MLRequest(models.Model):
    '''
    Keeps information about requests sent to ML algorithms.

    Attributes:
        input_data: Input data to the ML algorithm in JSON format.
        full_response: The response of the the ML Algorithm.
        response: Response of the ML algorithm in JSON format.
        feedback: Feedback about the response in JSON format.
        created_at: Date of request.
        parent_mlalgorithm: The ML algorithm used to compute the response.
    '''

    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE)
