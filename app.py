import random

print('''
        Mini RPG Adventure Game
''')

health = 10
heals_left = 5
attack_count = 0
block_count = 0

while health > 0:

    enemy_move = random.choice(["attack", "block"])
    game_order = input("Choose: attack - block - h to heal: ").lower()

    if game_order == "h":
        if heals_left > 0:
            heals_left -= 1
            health += 2
            print(f"You healed! Health is now {health}. Heals left: {heals_left}")
        else:
            print("No heals left!")
        continue

    if game_order == enemy_move:
        if game_order == "attack":
            attack_count += 1
        else:
            block_count += 1
        print(f"Great! You matched the enemy. (Attacks: {attack_count}, Blocks: {block_count})")

    elif game_order in ["attack", "block"]:
        health -= 1
        print(f"Oops! You got hit. Health is now {health}")

    else:
        print("Invalid input, try again.")

    if health <= 0:
        print("Unfortunately, you died. Game Over.")
        break
