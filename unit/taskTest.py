import unittest
import datetime
import todo

class TestTask(unittest.TestCase):

    def test_recognise_priorities(self):
        
        task = todo.Task("(A) Hello World")
        self.assertEqual(task.priority, "A")

    def test_recognise_priority_only_at_start(self):
        
        task = todo.Task("Hello World (A)")
        self.assertEqual(task.priority, None)

    def test_recognise_contexts(self):

        task = todo.Task("Hello World @test")
        self.assertEqual(task.contexts, ["@test"])

    def test_recognise_multiple_contexts(self):

        task = todo.Task("Hello World @task0 @task1")
        self.assertEqual(task.contexts, ["@task0","@task2"])
        
    def test_recognise_projects(self):

        task = todo.Task("Hello World +project")
        self.assertEqual(task.projects, ["+project"])

    def test_recognise_multiple_projects(self):

        task = todo.Task("Hello World +project0 +project1")
        self.assertEqual(task.projects, ["+project0", "+project1"])

    def test_original_task_retained(self):

        task = todo.Task("(A) Hell yeah! @herp +derp")
        self.assertEqual(task.original, "(A) Hell yeah! @herp +derp")

    def test_just_get_text(self):

        task = todo.Task("x 2013-02-10 (A) Hell yeah! @herp +derp")
        self.assertEqual(task.text, "Hell yeah!")

    def test_comparable(self):

        task0 = todo.Task("(A) This is a high task")
        task0.priority = "B"
        task1 = todo.Task("(B) This is a lower task")
        task1.priority = "A"

        self.assertTrue((task0 < task1))
        self.assertFalse((task0 > task1))
    
    def test_comparable_priority(self):

        task0 = todo.Task("This is a task")
        task0.priority = ""
        task1 = todo.Task("(B) This is a high task")
        task1.priority = "B"

        self.assertTrue((task0 < task1))
        self.assertFalse((task1 < task0))
        
    def test_recognise_dates(self):

        task = todo.Task("(D) 2012-02-14 I have a date!")
        self.assertEqual(task.date, datetime.date(2012, 2, 14))
        
    def test_recognise_dates_without_priority(self):

        task = todo.Task("2012-02-14 I have a date too!")
        self.assertEqual(task.date, datetime.date(2012, 2, 14))

    def test_return_none_no_date_present(self):

        task = todo.Task("I dont have a date")
        self.assertEqual(task.date, None)

    def test_no_recognise_bad_date(self):

        task = todo.Task("(A) 03-14-2014 This had a bad date")
        self.assertEqual(task.date, None)

    def test_recognise_done(self):

        task = todo.Task("x 2012-02-15 I'm finished")
        self.assertTrue(task.done)

    def test_recognise_not_done(self):

        task = todo.Task("2012-02-15 I'm not finished")
        self.assertFalse(task.done)

    def test_recognise_completion_date(self):

        task = todo.Task("x 2012-02-15 2012-02-14 I'm finished")
        self.assertTrue(task.date_done, datetime.date(2012, 2, 15))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTask))
    return suite
