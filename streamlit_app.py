import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Robot Thinking Process Visualizer")
    
    st. sidebar.header("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Home", "Graph Visualization", "Dashboard"])
    
    if page == "Home":
        st.subheader("Welcome to the Robot Thinking Process Visualizer")
        st.write("This application will help visualize how a robot processes information by mapping its thought nodes and connections.")
    
    elif page == "Graph Visualization":
        st.subheader("Graph Visualization")
        st.write("This section will display the visual representation of the robot's thought process.")
        # Placeholder for graph rendering functionality
        G = nx.DiGraph()
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        st.pyplot(plt)
    
    return G

def draw_graph(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    node_labels = nx.get_node_attributes(G, 'label')
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    st.pyplot(plt)

def main():
    st.title("Robot Thinking Process Visualizer")
    
    uploaded_file = st.file_uploader("Upload JSON file", type=["json"])
    
    if uploaded_file:
        json_data = load_json(uploaded_file)
        
        if json_data:
            st.subheader("Graph Visualization")
            G = create_graph(json_data)
            draw_graph(G)
            
            st.subheader("Raw JSON Data")
            st.json(json_data)
            
            st.subheader("Node and Edge Data")
            nodes_df = pd.DataFrame(json_data.get("nodes", []))
            edges_df = pd.DataFrame(json_data.get("edges", []))
            
            st.write("### Nodes")
            st.dataframe(nodes_df)
            
            st.write("### Edges")
            st.dataframe(edges_df)

if __name__ == "__main__":
    main()
