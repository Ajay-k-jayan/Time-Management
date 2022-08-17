from rest_framework import serializers
from .models import Task

# user serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields =  '__all__'
        fields = ('TaskId',
                  'TaskName',
                  'Status',
                  'StartTime',
                  'EndTime',
                  'CreatedDate',
                  'ApprovalStatus',
                  'AssignedManager',
                  'Description')