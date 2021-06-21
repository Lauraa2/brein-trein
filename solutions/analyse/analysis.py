    while counter > 0:
        print(counter)
        all_p = []
        all_score = []

        i = 0

        for i in range(1000):
            solution = random_alg.get_random_routes(data.stations, connections, time, counter)
            p = solution.calculate_fraction_connections()
            all_p.append(p)

            score = solution.calculate_score()
            all_score.append(score)

            i += 1

        with open(f'solutions/analyse/c={counter}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['p', all_p])
            writer.writerow(['score', all_score])

        counter += -1




    """
    Analyse
    """
    averages = []
    times = []
    
    
    for counter in range(1, 8):
        with open(f'solutions/analyse/c={counter}.csv') as file:
            reader = csv.reader(file)
            values = next(reader)
            values = values[1]
            values = values.strip('[]').split(', ')
            values = list(map(float, values))

            average = sum(values) / len(values)

            averages.append(float(average))
            times.append(counter)

    plt.plot(times, averages, marker='o', color='#5f8195')
    plt.axis([0, 8, 0, 0.7])
    plt.xlabel('aantal trajecten')
    plt.xticks([0, 1,2,3,4,5,6,7])
    plt.ylabel('gemiddelde p')
    plt.savefig('solutions/analyse/c_p(1).png')


    