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
    