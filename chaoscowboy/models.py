"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from django.db.models import Model, CharField, DateTimeField, ManyToManyField
from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import (
    AbstractUser)

class CowboyUser(AbstractUser):
    rax_username = models.CharField(max_length=16)
    rax_api_key = models.CharField(max_length=64)

class ActionTemplate(Model):
    name = CharField(max_length=255)
    plugin_type = CharField(max_length=63)
    parameters = JSONField()
    target = CharField(max_length=63)
    start_time = DateTimeField('Scheduled start time')


class ActionGroupTemplate(Model):
    name = CharField(max_length=255)
    start_time = DateTimeField('Scheduled start time')
    actions = ManyToManyField(ActionTemplate)


class CompletedAction(ActionTemplate):
    end_time = DateTimeField('Completed time')


class CompletedActionGroup(ActionGroupTemplate):
    end_time = DateTimeField('Completed time')


class QueuedAction(ActionTemplate):
    pass


class QueuedActionGroup(ActionGroupTemplate):
    pass
