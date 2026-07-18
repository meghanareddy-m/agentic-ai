import json

def save_results(results):

    with open("results.json","w") as file:
        json.dump(results,file,indent=4)

def stream_results(results):

    for result in results:
        print("Yielding result...")
        yield result