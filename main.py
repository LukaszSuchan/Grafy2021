import graph

while True:
    filename = str.strip(input("\nInsert path to graph file or type \"exit\" to exit: "))
    if str.lower(filename) == "exit":
        break

    graph = graph.Graph()
    errorMessage = graph.load(filename)
    if errorMessage is not None:
        print(errorMessage)
        continue

    start_index = input("Insert starting index: ")
    try:
        start_index = int(start_index)
    except:
        print("You did not enter a valid integer")
        continue
    if start_index > graph.vertices or start_index < 0:
        print("Vertex with this index does not belong to graph")
        continue

    # Executing algorithm and printing results
    graph.dijkstra(graph.graph, start_index)