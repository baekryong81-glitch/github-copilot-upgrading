import sqlite3

BASE = """CREATE TABLE IF NOT EXISTS _guachi_data (key PRIMARY KEY, value)"""
OPT_MAP = """CREATE TABLE IF NOT EXISTS _guachi_options (key PRIMARY KEY, value)"""
DEF_MAP = """CREATE TABLE IF NOT EXISTS _guachi_defaults (key PRIMARY KEY, value)"""

class dbdict(dict):
    # ...existing code...
