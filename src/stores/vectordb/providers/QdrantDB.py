from qdrant_client import models, QdrantClient
import logging
from ..VectorDBEnums import DiatanceMethodEnums
from ..VectorDBInterface import VectorDBInterface

class QdrantDB(VectorDBInterface):
    def __init__(self, db_path: str, distance_method: str):

        self.client = None
        self.db_path = db_path
        self.distance_method = None

        if distance_method == DiatanceMethodEnums.COSINE.value:
            self.distance_method = models.Distance.COSINE

        elif distance_method == DiatanceMethodEnums.DOT.value:
            self.distance_method = models.Distance.DOT

        self.logger = logging.getLogger(__name__)


    def connect(self):
        pass
        