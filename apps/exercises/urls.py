from django.conf.urls import patterns, url

from apps.exercises.views import ExerciseView

urlpatterns = patterns('',
                       url(r'^$', ExerciseView.as_view(), name='exercise_list'),
                       )
