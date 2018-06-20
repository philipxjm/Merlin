#!/usr/bin/env python3

import copy
import os
import random
import shutil
import sys

# TO DO: CLEAN UP THIS FILE, REMOVE LEGACY CODE, MAKE IT MORE GENERIC
# TO DO: ITERATE THROUGH PLAYERS RATHER THAN ROLES
# TO DO: POSSIBLY SPLIT EACH ROLE INTO A SEPARATE FILE/CLASS

DEFAULT_ROLES = dict()

DEFAULT_ROLES[5] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon"]}

DEFAULT_ROLES[6] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon"]}

DEFAULT_ROLES[7] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult",
        "Titania",
        "Arthur"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon"]}

DEFAULT_ROLES[8] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult",
        "Titania",
        "Arthur"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon",
        "Agravaine"]}

DEFAULT_ROLES[10] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult",
        "Titania",
        "Arthur"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon",
        "Agravaine",
        "Colgrevance"]}

DEFAULT_ROLES[11] = {
    'good': [
        "Merlin",
        "Percival",
        "Guinevere",
        "Lancelot",
        "Tristan",
        "Iseult",
        "Titania",
        "Arthur"],
    'evil': [
        "Mordred",
        "Morgana",
        "Maelegant",
        "Oberon",
        "Agravaine",
        "Colgrevance"]}

DEFAULT_TEAMS = dict()

DEFAULT_TEAMS[5] = {
    'good': 3,
    'evil': 2
}

DEFAULT_TEAMS[6] = {
    'good': 4,
    'evil': 2
}

DEFAULT_TEAMS[7] = {
    'good': 4,
    'evil': 3
}

DEFAULT_TEAMS[8] = {
    'good': 5,
    'evil': 3
}

DEFAULT_TEAMS[10] = {
    'good': 6,
    'evil': 4
}

DEFAULT_TEAMS[11] = {
    'good': 7,
    'evil': 4
}


class Thavalon:

    DEFAULT_ROLES = dict()

    DEFAULT_ROLES[5] = {
        'good': [
            "Merlin",
            "Percival",
            "Guinevere",
            "Lancelot",
            "Tristan",
            "Iseult"],
        'evil': [
            "Mordred",
            "Morgana",
            "Maelegant",
            "Oberon"]}

    DEFAULT_TEAMS = dict()

    DEFAULT_TEAMS[5] = {
        'good': 3,
        'evil': 2
    }

    def __init__(self, players, game_id):
        self.num_players = len(players)
        self.players = players
        self.players_to_roles = {}
        self.game_id = game_id

    def get_role_info(self):
        return self.players_to_roles

    def get_start_info(self):
        return self.first_proposal, self.second_proposal, self.third_proposal

    def roll(self, special_rules=None):

        starter_index = random.randint(0, len(self.players) - 1)

        self.first_proposal = self.players[starter_index - 2]
        self.second_proposal = self.players[starter_index - 1]
        self.third_proposal = self.players[starter_index]

        if special_rules:
            pass
        else:
            good_roles = copy.deepcopy(DEFAULT_ROLES[self.num_players]['good'])
            evil_roles = copy.deepcopy(DEFAULT_ROLES[self.num_players]['evil'])
            num_good = DEFAULT_TEAMS[self.num_players]['good']
            num_evil = DEFAULT_TEAMS[self.num_players]['evil']
        # shuffle the roles
        random.shuffle(good_roles)
        random.shuffle(evil_roles)

        # assign self.players to teams
        assignments = {}
        reverse_assignments = {}
        good_roles_in_game = set()
        evil_roles_in_game = set()
        roles_in_game = set()

        if self.num_players == 9:
            pelinor = self.players[8]
            assignments[pelinor] = "Pelinor"
            reverse_assignments["Pelinor"] = pelinor

            questing_beast = self.players[7]
            assignments[questing_beast] = "Questing Beast"
            reverse_assignments["Questing Beast"] = questing_beast

        good_players = self.players[:num_good]
        evil_players = self.players[num_good:num_good + num_evil]

        # assign good roles
        for good_player in good_players:
            player_role = good_roles.pop()
            assignments[good_player] = player_role
            reverse_assignments[player_role] = good_player
            good_roles_in_game.add(player_role)
            roles_in_game.add(player_role)

        # assign evil roles
        for evil_player in evil_players:
            player_role = evil_roles.pop()
            assignments[evil_player] = player_role
            reverse_assignments[player_role] = evil_player
            evil_roles_in_game.add(player_role)
            roles_in_game.add(player_role)

        # if "Lovers" in good_roles_in_game:
        # 	good_roles_in_game.remove("Lovers")
        # 	# lovers -> tristan
        # 	good_roles_in_game.add("Tristan")
        # 	good_roles_in_game.add("Iseult")
        # 	tristan_player = reverse_assignments["Lovers"]
        # 	assignments[tristan_player] = "Tristan"
        # 	del reverse_assignments["Lovers"]
        # 	reverse_assignments["Tristan"] = tristan_player
        # 	# random other good -> iseult
        # 	good_players_no_tristan = list(set(good_players))
        # 	good_players_no_tristan.remove(tristan_player)
        # 	iseult_player = str(random.sample(good_players_no_tristan, 1)[0])
        # 	old_role_iseult = assignments[iseult_player]
        # 	del reverse_assignments[old_role_iseult]
        # 	good_roles_in_game.remove(old_role_iseult)
        # 	assignments[iseult_player] = "Iseult"
        # 	reverse_assignments["Iseult"] = iseult_player

    # lone percival -> galahad
        if ("Percival" in good_roles_in_game
            and "Merlin" not in good_roles_in_game
            and "Morgana" not in evil_roles_in_game
                and self.num_players >= 7):
            good_roles_in_game.remove("Percival")
            good_roles_in_game.add("Galahad")
            percival_player = reverse_assignments["Percival"]
            assignments[percival_player] = "Galahad"
            del reverse_assignments["Percival"]
            reverse_assignments["Galahad"] = percival_player

        # missing roles
        missing_roles_good = list(set(good_roles) - set(good_roles_in_game))
        missing_roles_evil = list(set(evil_roles) - set(evil_roles_in_game))
        # print(missing_roles_good)
        # print(missing_roles_evil)

        oberon_target_role = ""
        oberon_seen = ""
        if ("Oberon" in evil_roles_in_game):
            good_roles_for_oberon = list(set(good_roles_in_game))
            if "Lancelot" in good_roles_in_game:
                good_roles_for_oberon.remove("Lancelot")
            if "Titania" in good_roles_in_game:
                good_roles_for_oberon.remove("Titania")
            if "Gawain" in good_roles_in_game:
                good_roles_for_oberon.remove("Gawain")
            random.shuffle(good_roles_for_oberon)
            oberon_target_role = good_roles_for_oberon[0]

        titania_target_role = ""
        titania_seen = ""
        if ("Titania" in good_roles_in_game):
            evil_roles_for_titania = list(set(evil_roles_in_game))
            random.shuffle(evil_roles_for_titania)
            titania_target_role = evil_roles_for_titania[0]

        if "Merlin" in good_roles_in_game:
            player_name = reverse_assignments["Merlin"]
            # determine who Merlin sees
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Mordred":
                    seen.append(evil_player)
            if "Lancelot" in good_roles_in_game:
                seen.append(reverse_assignments["Lancelot"])

            # oberon
            if oberon_target_role == "Merlin":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            # and write this info to Merlin's file
            info = ""
            info += "You are Merlin. "
            if oberon_target_role == "Merlin":
                info += " YOU HAVE BEEN OBERONED. You see one additional \
					     person who is neither Evil nor Lancelot.  "
            for seen_player in seen:
                info += "You see " + seen_player + " as evil (or Lancelot). "

            self.players_to_roles[player_name] = ("Merlin", info)

    # Percival sees Merlin, Morgana* as Merlin
        if "Percival" in good_roles_in_game:
            player_name = reverse_assignments["Percival"]
            # determine who Percival sees
            seen = []
            if "Merlin" in good_roles_in_game:
                seen.append(reverse_assignments["Merlin"])
            if "Morgana" in evil_roles_in_game:
                seen.append(reverse_assignments["Morgana"])
            # oberon
            if oberon_target_role == "Percival":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            # and write this info to Percival's file
            info = ""
            info += "You are Percival. "
            if oberon_target_role == "Percival":
                info += " YOU HAVE BEEN OBERONED. You see one additional \
						 person who is neither Merlin nor Morgana.  "
            for seen_player in seen:
                info += "You see " + seen_player + " as Merlin (or Morgana). "
            if len(seen) == 0:
                info += " Fin. "

            self.players_to_roles[player_name] = ("Percival", info)

        if "Tristan" in good_roles_in_game:
            # write the info to Tristan's file
            player_name = reverse_assignments["Tristan"]
            seen = []
            if "Iseult" in good_roles_in_game:
                seen.append(reverse_assignments["Iseult"])
            # oberon
            if oberon_target_role == "Tristan":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Tristan. "
            # write Iseult's info to file
            if oberon_target_role == "Tristan":
                info += "YOU HAVE BEEN OBERONED. You see one additional \
				         person who is not your lover. "
            for seen_player in seen:
                info += "You see " \
                    + seen_player \
                    + " as your luxurious lover Iseult. "
            if len(seen) == 0:
                info += "Nobody loves you. Not even your cat. "

            self.players_to_roles[player_name] = ("Tristan", info)

        if "Iseult" in good_roles_in_game:
            # write this info to Iseult's file
            player_name = reverse_assignments["Iseult"]
            seen = []
            if "Tristan" in good_roles_in_game:
                seen.append(reverse_assignments["Tristan"])
            # oberon
            if oberon_target_role == "Iseult":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Iseult. "
            # write Iseult's info to file
            if oberon_target_role == "Iseult":
                info += " YOU HAVE BEEN OBERONED. You see one additional \
				         person who is not your lover.  "
            for seen_player in seen:
                info += "You see " \
                    + seen_player \
                    + " as your luscious lover Tristan. "
            if len(seen) == 0:
                info += "Nobody loves you. "

            self.players_to_roles[player_name] = ("Iseult", info)

        if "Lancelot" in good_roles_in_game:
            # write ability to Lancelot's file
            player_name = reverse_assignments["Lancelot"]

            info = ""
            info += "You are Lancelot. You are on the Good team.   "
            info += "Ability: Reversal  "
            info += "You are able to play Reversal cards while on missions. \
					 A Reversal card inverts the result of a mission; a \
					 mission that would have succeeded now fails and vice \
					 versa.    "
            info += "Note: In games with at least 7 self.players, a Reversal \
					 played on the 4th mission results in a failed mission if \
					 there is only one Fail card, and otherwise succeeds. \
					 Reversal does not interfere with Agravaine's ability \
					 to cause the mission to fail "
            info += "So don't forget to reverse mission 4! "
            self.players_to_roles[player_name] = ("Lancelot", info)

        if "Guinevere" in good_roles_in_game:
            # guinevere sees two random "rumors"
            # rumors currently are only player knowledge (e.g. A sees B)

            player_name = reverse_assignments["Guinevere"]
            rumors = []
            truths = []
            lies = []
            connections = []

            not_guin = list(set(self.players) -
                            set([reverse_assignments["Guinevere"]]))
            if "Mordred" in evil_roles_in_game:
                not_guin.remove(reverse_assignments["Mordred"])

            for player in not_guin:
                other_players = list(set(not_guin) - set([player]))
                for other_player in other_players:
                    connections.append([player, other_player])

            # lies = list(set(connections)-set(truths))
            # lies = connections.remove(set(truths))

            evil_players_no_obemord = list(set(evil_players))
            evil_players_no_mordred = list(set(evil_players))
            if "Mordred" in evil_roles_in_game:
                evil_players_no_obemord.remove(reverse_assignments["Mordred"])
                evil_players_no_mordred.remove(reverse_assignments["Mordred"])
            if "Colgrevance" in evil_roles_in_game:
                evil_players_no_obemord.remove(
                    reverse_assignments["Colgrevance"])
            # rumor generation here
            for evil_player in evil_players_no_obemord:
                other_evil_players = list(
                    set(evil_players_no_obemord) - set([evil_player]))
                for evil_player_two in other_evil_players:
                    truths.append([evil_player, evil_player_two])
            if "Colgrevance" in evil_roles_in_game:
                oberon = reverse_assignments["Colgrevance"]
                for evil_player_not_oberon in evil_players_no_obemord:
                    truths.append([oberon, evil_player_not_oberon])
            if "Merlin" in good_roles_in_game:
                merlin = reverse_assignments["Merlin"]
                for evil_player_not_mordred in evil_players_no_mordred:
                    truths.append([merlin, evil_player_not_mordred])
                if "Lancelot" in good_roles_in_game:
                    lancelot = reverse_assignments["Lancelot"]
                    truths.append([merlin, lancelot])
            if "Percival" in good_roles_in_game:
                percival = reverse_assignments["Percival"]
                if "Merlin" in good_roles_in_game:
                    merlin = reverse_assignments["Merlin"]
                    truths.append([percival, merlin])
                if "Morgana" in evil_roles_in_game:
                    morgana = reverse_assignments["Morgana"]
                    truths.append([percival, morgana])
            if "Tristan" in good_roles_in_game:
                tristan = reverse_assignments["Tristan"]
                if "Iseult" in good_roles_in_game:
                    iseult = reverse_assignments["Iseult"]
                    truths.append([tristan, iseult])
                    truths.append([iseult, tristan])
            if "Arthur" in good_roles_in_game:
                arthur = reverse_assignments["Arthur"]
                guinevere = reverse_assignments["Guinevere"]
                good_players_no_arthur = list(
                    set(good_players) - set([arthur, guinevere]))
                for good_player in good_players_no_arthur:
                    truths.append([arthur, good_player])
            if "Galahad" in good_roles_in_game:
                galahad = reverse_assignments["Galahad"]
                for evil_player in evil_players_no_mordred:
                    truths.append([galahad, evil_player])

            lies = [lie for lie in connections if lie not in truths]
            random.shuffle(truths)
            random.shuffle(lies)

            guin_truths = []
            guin_lies = []
            if len(truths) > 0:
                new_truth = truths.pop(0)
                converse_truth = [new_truth[1], new_truth[0]]
                lies = [lie for lie in lies if lie != converse_truth]
                truths = [truth for truth in truths if truth != converse_truth]
                rumors.append(new_truth)
                guin_truths.append(new_truth)
                new_lie = lies.pop(0)
                converse_lie = [new_lie[1], new_lie[0]]
                lies = [lie for lie in lies if lie != converse_lie]
                truths = [truth for truth in truths if truth != converse_lie]
                rumors.append(new_lie)
                guin_lies.append(new_lie)

            guin_real_truths = copy.deepcopy(guin_truths)
            guin_real_lies = copy.deepcopy(guin_lies)

            if oberon_target_role == "Guinevere" and len(rumors) > 0:
                element = random.randint(0, 1)
                index = random.randint(0, 1)
                rumor = rumors[element]
                if index == 0:
                    oberon_seen = "<¿" + rumor[0] + "? -> " + rumor[1] + ">"
                if index == 1:
                    oberon_seen = "<" + rumor[0] + " -> ¿" + rumor[1] + "?>"
                rumor[index] = "???"
            random.shuffle(rumors)

            info = ""

            info += "You are Guinevere.  "
            if oberon_target_role == "Guinevere":
                info += " YOU HAVE BEEN OBERONED. One of your \
						 rumors has been corrupted.  "
            for rumor in rumors:
                info += "{} knows something about {}. ".format(
                    rumor[0], rumor[1])

            self.players_to_roles[player_name] = ("Guinevere", info)

        if "Titania" in good_roles_in_game:
            # write ability to Titania's file
            player_name = reverse_assignments["Titania"]

            info = ""

            info += "You are Titania.  "
            info += "You have added false information to the player with the role of " \
                + titania_target_role
            if "Oberon" in evil_roles_in_game:
                info += "There is an Oberon in the game. "

            self.players_to_roles[player_name] = ("Titania", info)

        if "Arthur" in good_roles_in_game:
            # determine which roles Arthur sees
            player_name = reverse_assignments["Arthur"]
            seen = []
            for good_role in good_roles_in_game:
                seen.append(good_role)
            # oberon
            if oberon_target_role == "Arthur":
                unseen = [
                    role for role in good_roles if role not in good_roles_in_game or role != "Arthur"]
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            # and write this info to Arthur's file
            info = ""

            info += "You are Arthur.  "
            if oberon_target_role == "Arthur":
                info += " YOU HAVE BEEN OBERONED. You see an additional good role that is not in the game.  "
            info += "The following good roles are in the game: "
            for seen_role in seen:
                if seen_role != "Arthur":
                    info += seen_role
            info += "Ability: Proclamation "
            info += "If two missions have failed, you may formally reveal that you are Arthur, establishing that you are Good for the remainder of the game. You may still propose and vote on missions, as well as be chosen to be part of a mission team, as per usual. "
            self.players_to_roles[player_name] = ("Arthur", info)

        if "Gawain" in good_roles_in_game:
            player_name = reverse_assignments["Gawain"]
            info = ""

            info += "You are Gawain. "
            info += " Ability: Once per game, after the 1st mission and before there are two missions with the same outcome (Pass or Fail), after the cards are chosen but before they are shuffled together, you may declare as Gawain. By doing so, you may collect the cards played by everyone except for the mission leader, shuffle them together and select one to remove. You then return the remaining cards to the mission leader, who shuffles the played cards and reveals the result. The card you removed does not affect the mission, but the next time you go on a mission, you must play the card you removed, even if you normally couldn't play it.  "
            info += " Note: If you remove a single Fail card, and Agravaine is on the mission, then Agravaine may declare and cause the mission to fail anyway. If Agravaine does this, you are no longer required to play a Fail card.  "

            self.players_to_roles[player_name] = ("Gawain", info)

        if "Galahad" in good_roles_in_game:
            # determine which roles Galahad sees
            seen = []
            for evil_role in evil_roles_in_game:
                seen.append(evil_role)
            random.shuffle(seen)
            if oberon_target_role == "Galahad":
                unseen = [
                    role for role in evil_roles if role not in evil_roles_in_game]
                random.shuffle(unseen)
                oberon_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            # and write this info to Arthur's file
            player_name = reverse_assignments["Galahad"]
            filename = "game/" + player_name

            info = ""
            info += "You are Galahad.  "
            if oberon_target_role == "Galahad":
                info += " YOU HAVE BEEN OBERONED. You see an additional evil role that is not in the game.  "

            info += "The following evil roles are in the game: "
            for seen_role in seen:
                info += seen_role
            info += " (The following roles are not in the game: Percival, Merlin, and Morgana.) "
            self.players_to_roles[player_name] = ("Galahad", info)

        # make list of evil self.players seen to other evil
        if "Colgrevance" in evil_roles_in_game:
            evil_players_no_oberon = list(
                set(evil_players) - set([reverse_assignments["Colgrevance"]]))
        else:
            evil_players_no_oberon = list(set(evil_players))

        random.shuffle(evil_players_no_oberon)

        if "Mordred" in evil_roles_in_game:
            player_name = reverse_assignments["Mordred"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)

            # titania
            if titania_target_role == "Mordred":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                titania_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""

            info += "You are Mordred. (Join us, we have jackets and meet on Thursdays. ~ Andrew and Kath) "
            if titania_target_role == "Mordred":
                info += " YOU HAVE BEEN TITANIA'D. You see one additional person who is not Evil.  "
            for seen_player in seen:
                if seen_player != player_name:
                    info += seen_player + " is a fellow member of the evil council. "
            if "Colgrevance" in evil_roles_in_game:
                info += "There is a Colgrevance lurking in the shadows. "

            self.players_to_roles[player_name] = ("Mordred", info)

        if "Morgana" in evil_roles_in_game:
            player_name = reverse_assignments["Morgana"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)

            # titania
            if titania_target_role == "Morgana":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                titania_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Morgana. "
            if titania_target_role == "Morgana":
                info += " YOU HAVE BEEN TITANIA'D. You see one additional person who is not Evil.  "

            for seen_player in seen:
                if seen_player != player_name:
                    info += seen_player + " is a fellow member of the evil council. "
            if "Colgrevance" in evil_roles_in_game:
                info += "There is an Colgrevance lurking in the shadows. "

            self.players_to_roles[player_name] = ("Morgana", info)

        if "Oberon" in evil_roles_in_game:
            player_name = reverse_assignments["Oberon"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)

            # titania
            if titania_target_role == "Oberon":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                titania_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Oberon. "
            if titania_target_role == "Oberon":
                info += " YOU HAVE BEEN TITANIA'D. You see one additional person who is not Evil.  "

            for seen_player in seen:
                if seen_player != player_name:
                    info += seen_player + " is a fellow member of the evil council. "

            info += "You have added false information to a good player. "

            self.players_to_roles[player_name] = ("Oberon", info)

        if "Agravaine" in evil_roles_in_game:
            player_name = reverse_assignments["Agravaine"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)
            # titania
            if titania_target_role == "Agravaine":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                titania_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Agravaine. "
            if titania_target_role == "Agravaine":
                info += " YOU HAVE BEEN TITANIA'D. You see one additional person who is not Evil.  "

            for seen_player in seen:
                if seen_player != player_name:
                    info += seen_player + " is a fellow member of the evil council. "
            if "Colgrevance" in evil_roles_in_game:
                info += "There is a Colgrevance lurking in the shadows. "

            info += " Ability: On any mission you are on, after the mission cards have been revealed, should the mission not result in a Fail (such as via a Reversal, requiring 2 fails, or other mechanics), you may formally declare as Agravaine to force the mission to Fail anyway.  "
            info += "Drawback: You may only play Fail cards while on missions. "
            self.players_to_roles[player_name] = ("Agravaine", info)

        if "Maelegant" in evil_roles_in_game:
            # write ability to Lancelot's file
            player_name = reverse_assignments["Maelegant"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)
            # titania
            if titania_target_role == "Maelegant":
                unseen = [
                    player for player in self.players if player not in seen]
                if (player_name in unseen):
                    unseen.remove(player_name)
                random.shuffle(unseen)
                titania_seen = unseen[0]
                seen.append(unseen[0])
            random.shuffle(seen)

            info = ""
            info += "You are Maelegant.   "
            if titania_target_role == "Maelegant":
                info += " YOU HAVE BEEN TITANIA'D. You see one additional person who is not Evil.  "

            for seen_player in seen:
                if seen_player != player_name:
                    info += seen_player + " is a fellow member of the evil council. "
            if "Colgrevance" in evil_roles_in_game:
                info += "There is a Colgrevance lurking in the shadows. "
            info += " Ability: Reversal  "
            info += "You are able to play Reversal cards while on missions. A Reversal card inverts the result of a mission; a mission that would have succeeded now fails and vice versa.    "
            info += "Note: In games with at least 7 self.players, a Reversal played on the 4th mission results in a failed mission if there is only one Fail card, and otherwise succeeds. Reversal does not interfere with Agravaine's ability to cause the mission to fail."

            self.players_to_roles[player_name] = ("Maelegant", info)

        if "Colgrevance" in evil_roles_in_game:
            player_name = reverse_assignments["Colgrevance"]
            filename = "game/" + player_name
            seen = []
            for evil_player in evil_players:
                if assignments[evil_player] != "Colgrevance":
                    seen.append(evil_player)
            titania_colgrevance_player = ""
            # titania
            if titania_target_role == "Colgrevance":
                if (player_name in seen):
                    seen.remove(player_name)
                random.shuffle(seen)
                titania_seen = seen[0]
                titania_colgrevance_player = seen[0]
            random.shuffle(seen)

            info += "You are Colgrevance. "
            if titania_target_role == "Colgrevance":
                info += " YOU HAVE BEEN TITANIA'D. One of your teammate's roles has been obscured.  "

            for seen_player in seen:
                if seen_player != player_name:
                    if seen_player != titania_colgrevance_player:
                        info += seen_player + " is " + \
                            assignments[seen_player] + ". "
                    else:
                        info += seen_player + " is ???. "

            self.players_to_roles[player_name] = ("Colgrevance", info)
