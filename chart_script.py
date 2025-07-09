import plotly.graph_objects as go

# Skills data from Gaurav Sharma's resume/portfolio
data = {
    "categories": [
        {
            "name": "Programming Languages",
            "skills": [
                {"skill": "Python", "proficiency": 90},
                {"skill": "Java", "proficiency": 80},
                {"skill": "JavaScript", "proficiency": 85},
                {"skill": "HTML/CSS", "proficiency": 90}
            ]
        },
        {
            "name": "Frameworks & Libraries",
            "skills": [
                {"skill": "React.js", "proficiency": 80},
                {"skill": "Pandas & NumPy", "proficiency": 85},
                {"skill": "Node.js", "proficiency": 75},
                {"skill": "Streamlit", "proficiency": 80}
            ]
        },
        {
            "name": "Databases & Tools",
            "skills": [
                {"skill": "MongoDB", "proficiency": 75},
                {"skill": "Git", "proficiency": 85},
                {"skill": "VS Code", "proficiency": 90},
                {"skill": "Jupyter Notebook", "proficiency": 85}
            ]
        }
    ]
}

# Brand colors for categories
colors = ['#1FB8CD', '#5D878F', '#13343B']

# Prepare chart data
skills = []
values = []
colors_list = []

for i, category in enumerate(data['categories']):
    for skill in category['skills']:
        skills.append(skill['skill'])
        values.append(skill['proficiency'])
        colors_list.append(colors[i])

# Reverse to show highest proficiency on top
skills.reverse()
values.reverse()
colors_list.reverse()

# Plotly chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=values,
    y=skills,
    orientation='h',
    marker_color=colors_list,
    text=[f"{v}%" for v in values],
    textposition='inside',
    textfont=dict(color='white', size=10),
    hovertemplate='<b>%{y}</b><br>%{x}%<extra></extra>',
    cliponaxis=False
))

# Layout updates
fig.update_layout(
    title='Gaurav Sharma - Technical Skills',
    xaxis_title='Proficiency %',
    yaxis_title='Skills',
    showlegend=False
)
fig.update_xaxes(range=[0, 100])
fig.update_yaxes(tickfont=dict(size=10))

# Save chart
fig.write_image('skills_chart.png')
print("Chart saved successfully!")
