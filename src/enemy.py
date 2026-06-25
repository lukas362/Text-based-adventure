# This file contains all enemys that you can encounter + their stats

# Variables for the diffrent enemys
enemy_goblin = "Goblin"
enemy_dog = "White Dog"
xp_given = "xp"

def enemy():
    return {}

def goblin():
    enemy_stats = {}
    enemy_stats["HP"] = 20
    enemy_stats["Attack"] = 5
    enemy_stats["xp"] = 20
    return enemy_stats

def white_dog():
    enemy_stats = {}
    enemy_stats["HP"] = 999
    enemy_stats["Attack"] = 999
    enemy_stats["xp"] = 999
    return enemy_stats