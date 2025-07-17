from generate_graph import generate_graph_plotly

def ui_draw(baseline, prediction, log=False):
    return generate_graph_plotly(baseline, prediction, log)
