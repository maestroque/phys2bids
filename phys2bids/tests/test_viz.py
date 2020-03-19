import os
from pkg_resources import resource_filename
from phys2bids.interfaces import txt
import wget
from phys2bids import viz


def test_plot_all():
    url = 'https://osf.io/sdz4n/download'  # url to Test_belt_pulse_samefreq.txt
    test_path = resource_filename('phys2bids', 'tests/data')
    test_filename = 'Test_belt_pulse_samefreq.txt'
    test_full_path = os.path.join(test_path, test_filename)
    wget.download(url, test_full_path)
    chtrig = 2
    phys_obj = txt.populate_phys_input(test_full_path, chtrig)
    out = os.path.join(test_path, 'Test_belt_pulse_samefreq.png')
    viz.plot_all(phys_obj, test_filename, outfile=out)
    assert os.path.isfile(out)
    os.remove(test_full_path)
    os.remove(out)


def test_plot_trigger():
    url = 'https://osf.io/sdz4n/download'  # url to Test_belt_pulse_samefreq.txt
    test_path = resource_filename('phys2bids', 'tests/data')
    test_filename = 'Test_belt_pulse_samefreq.txt'
    test_full_path = os.path.join(test_path, test_filename)
    wget.download(url, test_full_path)
    chtrig = 2
    out = os.path.join(test_path, 'Test_belt_pulse_samefreq')
    phys_obj = txt.populate_phys_input(test_full_path, chtrig)
    viz.plot_trigger(phys_obj.timeseries[0], phys_obj.timeseries[chtrig],
                     out, 1.5, 2.5, 0, test_filename)
    assert os.path.isfile(out + '_trigger_time.png')
    os.remove(test_full_path)
    os.remove(out + '_trigger_time.png')