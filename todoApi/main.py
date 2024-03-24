from fastapi import FastAPI , Depends , HTTPException
from model import Todo  , Updatetodo
from database import get_Session
from typing import Annotated
from sqlmodel import Session , select 





app = FastAPI( title= "todoApi" )




@app.post("/create/" , response_model=Todo)
def create_Todo(todo  : Todo , session : Annotated[ Session , Depends(get_Session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.get("/" , response_model= list[Todo])
def get_todo(session : Annotated[ Session , Depends(get_Session)]):
   data = session.exec(select(Todo)).all()
   return data

@app.put("/edit/{id}" )
def edit_todo(id : int  , newcontent :Updatetodo, session : Annotated[ Session , Depends(get_Session)]):
    
    query = select(Todo).where(id == Todo.id)
    result = session.exec(query).one()
    if not result:
        raise HTTPException(status_code=404  , detail="todo not found")
    result.content = newcontent.content
    session.add(result)
    session.commit()
    q = select(Todo).where(id == Todo.id)
    newdata = session.exec(q).one()
    return newdata


@app.delete("/delete/{id}")
def del_todo(id:int ,  session : Annotated[ Session , Depends(get_Session)]):
    query = select(Todo).where(id == Todo.id)
    re = session.exec(query).one()
    session.delete(re)
    session.commit()
    return "your todo has been deleted"



