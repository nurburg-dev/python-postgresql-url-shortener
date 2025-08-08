import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.pool = None
    
    async def create_pool(self):
        pass
    
    async def close_pool(self):
        pass
    
    async def execute(self, query: str, *args):
        pass
    
    async def fetch(self, query: str, *args):
        pass
    
    async def fetchrow(self, query: str, *args):
        pass
    
    async def fetchval(self, query: str, *args):
        pass

# Global database instance
database = Database()