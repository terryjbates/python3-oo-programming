#!/usr/bin/env python


####################################
# in a file called test_program.py #
####################################
from .assignment4  import ConfigDict, ConfigKeyError
import pytest
import os
import shutil

class TestConfigDict:
    config_file_template = './config_filename.template'
    config_file_working = './config_filename.txt'
    config_file_new = './config_filename_new.txt'
    config_file_bad = '/very_bad_path.txt'

    def setup_class(self):
        shutil.copy(TestConfigDict.config_file_template, TestConfigDict.config_file_working)

    def teardown_class(self):
        os.remove(TestConfigDict.config_file_working)
        os.remove(TestConfigDict.config_file_new)

    def test_obj(self):
        cd = ConfigDict('./config_filename.txt')
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)

    def test_existing_filename_and_attrib(self):
        assert os.path.isfile(TestConfigDict.config_file_working)
        cd = ConfigDict(TestConfigDict.config_file_working)
        assert os.path.isfile(TestConfigDict.config_file_working)

    def test_filename_existing(self):
        cd = ConfigDict(TestConfigDict.config_file_working)
        assert cd._filename == TestConfigDict.config_file_working

    def test_non_existing_filename(self):
        assert not os.path.isfile(TestConfigDict.config_file_new)
        cd = ConfigDict(TestConfigDict.config_file_new)
        assert cd._filename == TestConfigDict.config_file_new
        assert os.path.isfile(TestConfigDict.config_file_new)

    def test_bad_file_path(self):
        with pytest.raises(IOError):
            ConfigDict(TestConfigDict.config_file_bad)

    def test_read_dict(self):
        cd = ConfigDict(TestConfigDict.config_file_working)
        assert cd['bacon'] == 'father'
        assert cd['blaise'] == 'matuidi'
        assert cd['blass'] == 'reiter'

        with pytest.raises(ConfigKeyError):
            print(cd['bowie'])

    def test_write_dict(self):
        cd = ConfigDict(TestConfigDict.config_file_working)
        cd['bowie'] = 'blackstar'
        cd2 = ConfigDict(TestConfigDict.config_file_working)
        assert cd2['bowie'] == 'blackstar'