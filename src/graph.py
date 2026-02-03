from langgraph.graph import StateGraph

class LaunchState(dict):
    pass

def human_approval(state: LaunchState):
    print("\n--- HUMAN APPROVAL STEP ---")
    input("Press ENTER to approve and continue...")
    return state

graph = StateGraph(LaunchState)
graph.add_node("approval", human_approval)
graph.set_entry_point("approval")

launch_graph = graph.compile()
