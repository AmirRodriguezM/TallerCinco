from fastapi import FastAPI
import mook

app = FastAPI()

@app.get("/")

def root():

    return {

        "Servicio": "Estructuras de datos"

    }

@app.post("/indices-invertidos")

def indices_invertidos(palabra: dict):

    mook.my_documents

    cache={}

    for index, documento in enumerate(mook.my_documents):

        words= documento.lower().split()
        for word in words:
            if word in cache:
                cache[word].append(documento)

            else:
                cache[word] = [documento]


    print(cache)

    return cache.get(palabra["palabra"],"No se encontro")