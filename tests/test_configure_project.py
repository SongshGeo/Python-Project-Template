#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

"""Tests for the configure_project script."""

from unittest.mock import patch

import pytest

from scripts.configure_project import (
    configure_files,
    main,
    setup_description_files,
)


class TestConfigureFiles:
    """Test configure_files function."""

    @patch("scripts.configure_project.Path.write_text")
    @patch("scripts.configure_project.Path.read_text")
    @patch("scripts.configure_project.Path.exists")
    def test_configure_files_updates_pyproject(
        self, mock_exists, mock_read_text, mock_write_text
    ):
        """Test that configure_files updates pyproject.toml correctly."""
        # Setup
        mock_exists.return_value = True
        mock_read_text.return_value = (
            'name = "old-name"\ndescription = "Old description"'
        )

        # Run
        configure_files("new-project", "New description")

        # Assert - read_text should be called at least once
        assert mock_read_text.call_count >= 1
        # write_text should be called at least once
        assert mock_write_text.call_count >= 1

    @patch("scripts.configure_project.Path.exists")
    @patch("scripts.configure_project.print")
    def test_configure_files_with_missing_file(self, mock_print, mock_exists):
        """Test configure_files handles missing files gracefully."""
        # Setup - file doesn't exist
        mock_exists.return_value = False

        # Run - should not crash
        configure_files("test-project", "Test description")

        # Assert - print should be called to indicate file not found
        mock_print.assert_called()


class TestSetupDescriptionFiles:
    """Test setup_description_files function."""

    @patch("scripts.configure_project.Path.write_text")
    def test_setup_description_files(self, mock_write_text):
        """Test that setup_description_files creates files."""
        # Run
        setup_description_files("Test Project", "Test Description")

        # Assert
        assert mock_write_text.call_count == 2


class TestMain:
    """Test main function."""

    @patch("scripts.configure_project.setup_description_files")
    @patch("scripts.configure_project.configure_files")
    @patch("scripts.configure_project.questionary")
    @patch("scripts.configure_project.print")
    def test_main_function_calls(
        self, mock_print, mock_questionary, mock_configure, mock_setup
    ):
        """Test that main function calls all required functions."""
        # Setup
        mock_questionary.text.return_value.ask.return_value = "test-project"

        # Run
        main()

        # Assert
        mock_configure.assert_called_once()
        mock_setup.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
