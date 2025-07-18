import plotly.graph_objs as go

def generate_graph_plotly(base_value, prediction_values, log_scale=False):
    x_values = list(range(len(prediction_values)))
    y_values = prediction_values

    trace = go.Scatter(
        x=x_values,
        y=y_values,
        mode='lines+markers',
        name='Transistor Count Prediction'
    )

    layout = go.Layout(
        title='Moore\'s Law Transistor Growth',
        xaxis=dict(title='Years Elapsed'),
        yaxis=dict(title='Transistors', type='log' if log_scale else 'linear')
    )

    fig = go.Figure(data=[trace], layout=layout)
    return fig
