from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from accounts.models import User
from .serializers import JobSerializer, JobCreationSerializer


@api_view(['GET'])
def job_list(request):
    job_object = Job.objects.all()
    serializer = JobSerializer(job_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def job_details(request, id):
    job = Job.objects.get(pk=id)
    serializer = JobSerializer(job)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def job_create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    _mutable = request.POST._mutable
    request.POST._mutable = True
    # request.POST['created_by'] = request.user.id
    serializer = JobCreationSerializer(context={'request': request}, data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors
    return Response(**response)


@api_view(['PUT', 'PATCH'])
def job_edit(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    if job.created_by.id != request.user.id:
        response['data'] = {'error': 'You are not authorized to edit this job'}
    else:
        if request.method == 'PUT':
            serializer = JobSerializer(instance=job, data=request.data)
        else:
            serializer = JobSerializer(instance=job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_201_CREATED
        else:
            response['data'] = serializer.errors
    return Response(**response)


@api_view(['DELETE'])
def job_delete(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    if job.created_by.id != request.user.id:
        response['data'] = {'error': 'You are not authorized to edit this job'}
    else:
        job.delete()
        response['data'] = {'success': 'Job deleted successfully'}
        response['status'] = status.HTTP_200_OK
    return Response(**response)


@api_view(['POST'])
def accept_developer(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    if job.created_by.id != request.user.id:
        response['data'] = {'error': 'You are not authorized to edit this job'}
    else:
        job.developer = User.objects.get(pk=request.data['developer_id'])
        job.status = 'in_progress'
        job.save(update_fields=['developer_id'])
        response['data'] = {'success': 'Developer accepted successfully'}
        response['status'] = status.HTTP_200_OK
    return Response(**response)


@api_view(['POST'])
def apply_job(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    job.applied_developers.add(request.user.id)
    response['data'] = {'success': 'Job applied successfully'}
    response['status'] = status.HTTP_200_OK
    return Response(**response)


@api_view(['POST'])
def finish_job(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    if job.developer == request.user:
        job.status = 'ﬁnished'
        job.save(update_fields=['status'])
        response['data'] = {'success': 'Job finished successfully'}
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'Unauthorized'}
    return Response(**response)

