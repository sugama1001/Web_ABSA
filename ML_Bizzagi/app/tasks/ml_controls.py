from celery import shared_task

@shared_task(ignore_result=False)
def queue_process(a: int, b: int) -> int:
    return a + b

@shared_task(ignore_result=False)
def queue_process(a: int, b: int) -> int:
    return a + b