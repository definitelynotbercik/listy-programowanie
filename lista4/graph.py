import networkx as nx
import matplotlib.pyplot as plt
import random
import imageio as iio
import os


def agent_walk(agent_position, steps, graph):
    for i in range(steps):
        nb = list(nx.neighbors(graph, agent_position))
        if nb == []:
            continue
        else:
            agent_position = random.choice(nb)
        node_colors = ["r" if node == agent_position else "b" for node in graph.nodes()]
        plt.title(f"step {i}")
        nx.draw_shell(graph, with_labels=True, node_color=node_colors)
        plt.savefig(f"C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images\\agent_walk{i}.jpg",
                    transparent=False,
                    facecolor="white")
        plt.clf()


def make_gif(gif_folder, gif_name):
    im_to_gif = len(os.listdir(gif_folder))
    frames = []
    for i in range(im_to_gif):
        image = iio.v3.imread(f"C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images\\agent_walk{i}.jpg")
        frames.append(image)
    iio.mimsave(f"C:\\Users\\zawer\\Documents\\python1\\extras\\{gif_name}.gif",
                frames,
                duration=1000,
                loop=0)
    

def clear_directory(directory):
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))


def make_random_graph():
    G = nx.gnp_random_graph(6, 0.4)
    agent_position = random.choice(list(nx.nodes(G)))

    agent_walk(agent_position, 10, G)
    make_gif("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images", "random_graph")
    clear_directory("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images")


def make_watts_strogatz_graph():
    G = nx.watts_strogatz_graph(6, 2, 0.3)
    agent_position = random.choice(list(nx.nodes(G)))

    agent_walk(agent_position, 10, G)
    make_gif("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images", "watts_strogatz_graph")
    clear_directory("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images")


def make_barabasi_albert_graph():
    G = nx.barabasi_albert_graph(6, 2)
    agent_position = random.choice(list(nx.nodes(G)))

    agent_walk(agent_position, 10, G)
    make_gif("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images", "barabasi_albert_graph")
    clear_directory("C:\\Users\\zawer\\Documents\\python1\\extras\\graph_images")


if __name__ == "__main__":
    make_random_graph()
    make_watts_strogatz_graph()
    make_barabasi_albert_graph()