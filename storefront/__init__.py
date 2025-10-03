# Loading the celery module in init module of the current package 
# So that its discovered and excuted

from .celery import celery
