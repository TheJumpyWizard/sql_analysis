from fastapi import APIRouter
from schemas.query import Query
from sql_analysis.parser import generate_data_lineage

router = APIRouter()


@router.post("/parse")
async def parse_query(query: Query):
    graph = await generate_data_lineage(query.query)
    return {"graph": graph.adj}

