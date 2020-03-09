from matplotlib.pyplot import pie, show, axis

def draw_pie_chart(sizes, labels):
    pie(sizes, labels = labels)
    axis('equal')
    show()

def main():
    sizes = [1, 4, 4, 5, 6]
    labels = ['Drama', 'Sci-Fi', 'Comedy', 'Action', 'Romance']

    draw_pie_chart(sizes, labels)

if __name__ == "__main__":
    main()
