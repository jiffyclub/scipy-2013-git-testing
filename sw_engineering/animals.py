def mean_animals(filename, kind):
    """
    Calculates the mean number of a particular animal seen per sighting using
    the data in the given file.

    Parameters
    ----------
    filename : str
        Path to file to use.
    kind : str
        Species of animal for which to calculate average
        number seen per sighting.

    Returns
    -------
    mean : float
        Mean number of animal seen per sighting.

    """
    date, time, species, count = read_animals(filename)
    date, time, species, count = \
        filter_animals_by_kind(kind, date, time, species, count)
    return mean(count)


def read_animals(filename):
    """
    Reads an animals.txt type file. Returns four lists, one per column.

    Parameters
    ----------
    filename : str
        The name of an animals.txt type file.

    Returns
    -------
    dates : list of str
    times : list of str
    species : list of str
    counts : list of int

    """
    f = open(filename)
    dates = []
    times = []
    species = []
    counts = []

    for line in f:
        d, t, s, c = line.split()
        dates.append(d)
        times.append(t)
        species.append(s)
        counts.append(int(c))

    f.close()

    return dates, times, counts, species


def mean(nums):
    """
    Calculates the mean of a list of numbers.

    Parameters
    ----------
    nums : list of numbers

    Returns
    -------
    m : number

    """
    # fill this in


def filter_animals_by_kind(kind, date, time, species, count):
    """
    Filter the animals dataset to only include data for a given species
    of animal.

    Parameters
    ----------
    kind : str
        Species of animal to filter on.
    date : list of str
    time : list of str
    species : list of str
    count : list of int

    Returns
    -------
    filtered_date : list of str
    filtered_time : list of str
    filtered_species : list of str
    filtered_count : list of int

    """
    # fill this in
