import unittest
from unittest.mock import patch, MagicMock
from AIModelsList import list_models

class TestAIModelsList(unittest.TestCase):

    @patch('AIModelsList.ModelManager')
    def test_list_models(self, MockModelManager):
        # Create a mock instance
        mock_instance = MagicMock()
        MockModelManager.return_value = mock_instance
        
        # Define the mock return value for list_models
        mock_instance.list_models.return_value = ['model1', 'model2', 'model3']
        
        # Call the function
        models = list_models()
        
        # Assertions
        self.assertEqual(models, ['model1', 'model2', 'model3'])
        mock_instance.list_models.assert_called_once()

if __name__ == "__main__":
    unittest.main()
