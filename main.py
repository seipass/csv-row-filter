from __future__ import annotations
def run(rows,column,value):
 return [r for r in rows if r.get(column)==value]
