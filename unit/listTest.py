import unittest
import todo
import sys, os

class TestList(unittest.TestCase):

    def setUp(self):
        """
        Provides some setup, including a list to work off
        """
        
        test_data = ["(A) Thank Mom for the meatballs @phone",
                "(B) Schedule Goodwill pickup +GarageSale @phone",
                "(B) Post signs around the neighborhood +GarageSale",
                "@GroceryStore Eskimo pies",
                "2011-03-02 Document +TodoTxt task format",
                "x 2011-03-03 Call Mom",
                "x 2011-03-02 2011-03-01 Review Tim's pull request +TodoTxtTouch @github"]

        self.todo_list = todo.TaskList(test_data)


    def test_items_are_tasks(self):

        for item in self.todo_list:
            assetIsInstance(item, todo.Task)
            
    def test_filter_by_priority(self):

        for item in self.todo_list.by_priority("B"):
            assertEqual("B", item.priority)

    def test_filter_by_context(self):

        for item in self.todo_list.by_context("@phone"):
            assertTrue("@phone" in item.projects)
            
    def test_filter_by_project(self):

        for item in self.todo_list.by_project("+GarageSale"):
            assertTrue("+GarageSale" in item.projects)
            
    def test_filter_by_all_three(self):

        for item in self.todo_list.by_context("@phone").by_project("+GarageSale").by_priority("B"):
            assertTrue("+GarageSale" in item.projects)
            assertTrue("@phone" in item.contexts)
            assertEqual("B" in item.projects)
            
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestList))
    return suite

