from checkers import checkout, getout
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class TestPositive:
    """Класс, содержащий положительные тестовые случаи"""

    def test_step1(self, make_folders, clear_folders, make_files, print_time):
        """Test case 1"""
        res1 = checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx -t{data['type']}",
                        "Everything is Ok")
        res2 = checkout(f"ls {data['folder_out']}", "arx.{}".format(data['type']))
        assert res1 and res2, "test1 FAIL"

    def test_step2(self, clear_folders, make_files):
        """Test case 2"""
        res = []
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx -t{data['type']}",
                            "Everything is Ok"))
        res.append(checkout(f"cd {data['folder_out']}; 7z e arx.{data['type']} -o{data['folder_ext']} -y",
                            "Everything is Ok"))
        for item in make_files:
            res.append(checkout(f"ls {data['folder_ext']}", item))
        assert all(res)

    def test_step3(self):
        """Test case 3"""
        assert checkout(f"cd {data['folder_out']}; 7z t arx.{data['type']}", "Everything is Ok"), "test3 FAIL"

    def test_step4(self):
        """Test case 4"""
        assert checkout(f"cd {data['folder_in']}; 7z u arx2.{data['type']}", "Everything is Ok"), "test4 FAIL"

    def test_step5(self, clear_folders, make_files):
        """Test case 5"""
        res = []
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx -t{data['type']}",
                            "Everything is Ok"))
        for i in make_files:
            res.append(checkout(f"cd {data['folder_out']}; 7z l arx.{data['type']}", i))
        assert all(res), "test5 FAIL"

    def test_step6(self, clear_folders, make_files, make_subfolder):
        """Test case 6"""
        res = []
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx -t{data['type']}",
                            "Everything is Ok"))
        res.append(checkout(f"cd {data['folder_out']}; 7z x arx.{data['type']} -o{data['folder_ext2']} -y",
                            "Everything is Ok"))
        for i in make_files:
            res.append(checkout(f"ls {data['folder_ext2']}", i))
        res.append(checkout(f"ls {data['folder_ext2']}/{make_subfolder[0]}", make_subfolder[1]))
        assert all(res), "test6 FAIL"

    def test_step7(self):
        """Test case 7"""
        assert checkout(f"cd {data['folder_out']}; 7z d arx.{data['type']}", "Everything is Ok"), "test7 FAIL"

    def test_step8(self, clear_folders, make_files):
        """Test case 8"""
        res = []
        for i in make_files:
            res.append(checkout(f"cd {data['folder_in']}; 7z h {i}", "Everything is Ok"))
            hash = getout(f"cd {data['folder_in']}; 7z h {i}").upper()
            res.append(checkout(f"cd {data['folder_in']}; 7z h {i}", hash))
        assert all(res), "test8 FAIL"