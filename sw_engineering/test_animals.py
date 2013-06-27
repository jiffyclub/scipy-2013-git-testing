import animals


def test_read_animals():
    ref_dates = ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']
    ref_times = ['21:06', '14:12', '10:24', '20:08', '18:46']
    ref_species = ['Grizzly', 'Elk', 'Elk', 'Wolverine', 'Muskox']
    ref_counts = [36, 25, 26, 31, 20]

    dates,times,species,counts = animals.read_animals('animals.txt')

    assert dates == ref_dates
    assert times == ref_times
    assert species == ref_species
    assert counts == ref_counts

def test_mean():
    assert animals.mean([0,1]) == .5
    assert animals.mean([-4,6]) == 1
    assert animals.mean([0, 1.5, 4.5]) == 2
    assert animals.mean([5]) == 5
    assert animals.mean([-5,-15,-10]) == -10
    assert animals.mean([1e6,1e7]) == 5.5e6
    assert animals.mean([-4,2,4,-2]) == 0


def test_filter_animals():
    date, time, species, count = animals.read_animals('animals.txt')
    kind = 'Grizzly'
    d, t, s, c = animals.filter_animals_by_kind(kind, date, time, species, count)

    assert d == ['2011-04-22']
    assert t == ['21:06']
    assert s == ['Grizzly']
    assert c == [36]

    kind = 'Elk'
    d, t, s, c = animals.filter_animals_by_kind(kind, date, time, species, count)

    assert d == ['2011-04-23', '2011-04-23']
    assert t == ['14:12', '10:24']
    assert s == ['Elk', 'Elk']
    assert c == [25, 26]


def test_mean_animals():
    mean = animals.mean_animals('animals.txt', 'Grizzly')
    assert mean == 36

    mean = animals.mean_animals('animals.txt', 'Elk')
    assert mean == 25.5

