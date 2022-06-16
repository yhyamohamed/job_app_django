from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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
    if request.user.user_type == 'developer':
        response['data'] = {'message':'You are not authorized to create job'}
    else:
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
    if job.created_by.id != request.user.id and job.status != "open":
        response['data'] = {'error': 'You are not authorized to edit this job or job already open'}
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

    if job.created_by.id != request.user.id and job.status != "open":
        response['data'] = {'error': 'You are not authorized to delete this job or job already open'}
    else:
        job.delete()
        response['data'] = {'success': 'Job deleted successfully'}
        response['status'] = status.HTTP_200_OK
    return Response(**response)


@api_view(['POST'])
def accept_developer(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    developer_applied = job.applied_developers.filter(pk=request.data['developer_id'])
    if job.created_by.id != request.user.id and job.status != "open":
        response['data'] = {'error': 'You are not authorized to edit this job or job already open'}
    elif not developer_applied:
        response['data'] = {'Error': 'Developer didnot apply for this job'}
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
    if request.user.user_type == 'recruiter':
        response['data'] = {'message':'You are not authorized to apply for job'}
    else:
        job = Job.objects.get(pk=id)
        jobs = Job.objects.all()
        all_developer_applied = jobs.filter(applied_developers__id=request.user.id)
        if not all_developer_applied:
            job.applied_developers.add(request.user.id)
            response['data'] = {'success': 'Developer applied successfully'}
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = {'Error': 'Developer already applied for a job'}
    return Response(**response)


@api_view(['POST'])
def finish_job(request, id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job = Job.objects.get(pk=id)
    if job.developer == request.user or job.created_by == request.user:
        job.status = 'ﬁnished'
        job.save(update_fields=['status'])
        response['data'] = {'success': 'Job finished successfully'}
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'you are not authrized'}
    return Response(**response)

