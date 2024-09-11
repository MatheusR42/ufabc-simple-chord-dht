from protocols import meu_qoelho_mq_pb2
from db import DB
from models import Queue
from typing import Dict, List
from time import sleep

class QueueService:
  queues_map: Dict[str, Queue] = {}
  db: DB

  def __init__(self, db: DB):
    self.db = db
    self.queues_map = self.db.find_queues()

  def join(self) -> Queue:
      print("QueueService: join")
      return meu_qoelho_mq_pb2.Empty()
