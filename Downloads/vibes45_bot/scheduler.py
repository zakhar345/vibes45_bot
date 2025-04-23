from apscheduler.schedulers.asyncio import AsyncIOScheduler

def setup_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.start()
