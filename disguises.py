class Disguise:

    def __init__(self, name, color_requirements, mana_value, power, toughness, blocks_flying, image):
        self.name = name
        self.color_requirements = color_requirements
        self.mana_value = mana_value
        self.power = power
        self.toughness = toughness
        self.image = image
        self.blocks_flying = blocks_flying

    def castable(self, mana_sources):
        if len(mana_sources) <= self.mana_value:
            return False
        i = 0
        color_requirement = self.color_requirements.copy()
        while len(color_requirement) > 0:
            current = mana_sources[i]
            if (current == 'rainbow') or (color_requirement[0] in current) or (color_requirement[-1] in current):
                color_requirement.pop()
            i += 1
            if i >= len(mana_sources):
                return False
        return True

disguise_list = []
disguise_list.append(Disguise("Aurelia's Vindicator", ['W'], 4, 4, 2, True, 'https://cards.scryfall.io/normal/front/5/9/5901dff4-e09b-4747-9297-797a1a057cd5.jpg?1706241453'))
disguise_list.append(Disguise("Defenestrated Phantom", ['W'], 5, 4, 3, True, 'https://cards.scryfall.io/normal/front/8/b/8b284304-c3bf-4413-9fd3-b44eb4eb642a.jpg?1706572515'))
disguise_list.append(Disguise("Essense of Antiquity", ['W'], 3, 1, 10, False, 'https://cards.scryfall.io/normal/front/a/e/aee2945d-bf6d-4328-a482-df24c2973b56.jpg?1706241485'))
disguise_list.append(Disguise("Forum Familiar", ['W'], 2, 2, 2, False, 'https://cards.scryfall.io/normal/front/b/0/b06a243d-acc8-42cd-926c-98a4cc96ab21.jpg?1706241486'))

disguise_list.append(Disguise("Museum Nightwatch", ['W'], 2, 3, 2, False, 'https://cards.scryfall.io/normal/front/3/7/37860682-4973-4a0f-a43a-3056037bd2dc.jpg?1706241514'))
disguise_list.append(Disguise("Unyielding Gatekeeper", ['W'], 2, 3, 2, False, 'https://cards.scryfall.io/normal/front/f/3/f3a0d597-d2df-4aaf-8084-c8eeda64ce60.jpg?1706241543'))
disguise_list.append(Disguise("Bubble Smuggler", ['U'], 6, 6, 5, False, 'https://cards.scryfall.io/normal/front/6/b/6b863ee0-d9f3-4b1e-993d-5212731d9353.jpg?1706241560'))
disguise_list.append(Disguise("Coveted Falcon", ['U'], 4, 4, 2, True, 'https://cards.scryfall.io/normal/front/b/c/bc936987-d58b-4e7c-870f-379bcae77727.jpg?1706241580'))

disguise_list.append(Disguise("Exit Specialist", ['U'], 2, 2, 1, False, 'https://cards.scryfall.io/normal/front/2/6/268f142d-9fb1-4673-b804-add1f08dacb9.jpg?1706241600'))
disguise_list.append(Disguise("Mistway Spy", ['U'], 2, 1, 1, True, 'https://cards.scryfall.io/normal/front/e/8/e8578839-046f-4afd-a0e7-4737ded9e6eb.jpg?1706241631'))
disguise_list.append(Disguise("Alley Assailant", ['B'], 6, 3, 3, False, 'https://cards.scryfall.io/normal/front/e/d/edf238c9-61de-4f3a-b82f-05af46e5e81b.jpg?1706241664'))
disguise_list.append(Disguise("Basilica Stalker", ['B'], 5, 3, 4, True, 'https://cards.scryfall.io/normal/front/f/d/fdafea8f-283d-4f19-a74a-669bfbdfed98.jpg?1706241669'))

disguise_list.append(Disguise("Hunted Bonebrute", ['B'], 2, 6, 2, False, 'https://cards.scryfall.io/normal/front/a/4/a4ca0e10-8b7c-4ce2-888b-752fc909757a.jpg?1706241698'))
disguise_list.append(Disguise("Nightdrinker Moroii", ['B', 'B'], 2, 4, 2, True, 'https://cards.scryfall.io/normal/front/c/e/ce043cba-aea4-4156-b1d0-545eda06c400.jpg?1706241726'))
disguise_list.append(Disguise("Bolrac-Clan Basher", ['R', 'R'], 5, 6, 2, False, 'https://cards.scryfall.io/normal/front/b/8/b87683f7-8a61-4e4a-8b8b-3bf812454096.jpg?1706241824'))
disguise_list.append(Disguise("Concealed Weapon", ['R'], 3, 3, 0, False, 'https://cards.scryfall.io/normal/front/3/8/38e31fa6-a445-47c6-a73f-135087f6d760.jpg?1706241834'))

disguise_list.append(Disguise("Fugitive Codebreaker", ['R'], 1, 2, 1, False, 'https://cards.scryfall.io/normal/front/b/6/b682bf8a-06dc-4828-bc46-9e1427bf981f.jpg?1706241868'))
disguise_list.append(Disguise("Offender at Large", ['R'], 5, 5, 4, False, 'https://cards.scryfall.io/normal/front/f/0/f096ff4a-85f4-46f1-9478-e8921f21309d.jpg?1706241900'))
disguise_list.append(Disguise("Pyrotechnic Performer", ['R'], 1, 3, 2, False, 'https://cards.scryfall.io/normal/front/0/f/0fa5671b-2651-4944-a50a-c768ec70229e.jpg?1706241909'))
disguise_list.append(Disguise("Culvert Ambusher", ['G'], 5, 4, 5, False, 'https://cards.scryfall.io/normal/front/2/c/2ccdc58b-1e7e-402c-88f9-c789ff1dae31.jpg?1706241967'))

disguise_list.append(Disguise("Flourishing Bloom-Kin", ['G'], 5, 0, 0, False, 'https://cards.scryfall.io/normal/front/5/d/5ddcb31e-9301-44f1-b138-0573fbf56a47.jpg?1706241970'))
disguise_list.append(Disguise("Greenbelt Radical", ['G', 'G'], 7, 5, 5, False, 'https://cards.scryfall.io/normal/front/8/8/88e62346-cc62-4938-970c-b56beeb79fa6.jpg?1706241982'))
disguise_list.append(Disguise("Nervous Gardener", ['G'], 1, 2, 2, False, 'https://cards.scryfall.io/normal/front/9/3/93b747c7-b342-47f8-a190-16c393b20607.jpg?1706242060'))
disguise_list.append(Disguise("Vengeful Creeper", ['G'], 6, 5, 5, False, 'https://cards.scryfall.io/normal/front/7/a/7a914416-effd-4eda-b609-2773c53a08ec.jpg?1706242102'))

disguise_list.append(Disguise("Crowd-Control Warden", ['GW', 'GW'], 5, 4, 4, False, 'https://cards.scryfall.io/normal/front/c/d/cdf0578f-4966-4ecd-81e1-83ae13126f13.jpg?1706242133'))
disguise_list.append(Disguise("Dog Walker", ['RW', 'RW'], 2, 3, 1, False, 'https://cards.scryfall.io/normal/front/a/6/a6e0adb7-a030-4dcc-9284-cd91c7598a22.jpg?1706242142'))
disguise_list.append(Disguise("Faerie Snoop", ['UB', 'UB'], 3, 1, 4, True, 'https://cards.scryfall.io/normal/front/2/0/20267dab-8898-4b44-8ef4-8a239967662c.jpg?1706242161'))
disguise_list.append(Disguise("Gadget Technician", ['UR', 'UR'], 2, 4, 3, True, 'https://cards.scryfall.io/normal/front/3/b/3b489a54-ee43-4962-be7b-16e0e28800e0.jpg?1706242168'))

disguise_list.append(Disguise("Granite Witness", ['UW', 'UW'], 2, 3, 2, True, 'https://cards.scryfall.io/normal/front/d/a/daee9d98-f8c6-4980-8f23-c6c636b69430.jpg?1706242170'))
disguise_list.append(Disguise("Rakish Scoundrel", ['GB', 'GB'], 6, 3, 3, False, 'https://cards.scryfall.io/normal/front/6/a/6aaa8c6b-7ef7-45db-99c9-4a6e7f177b94.jpg?1706242231'))
disguise_list.append(Disguise("Riftburst Hellion", ['RG', 'RG'], 6, 6, 7, True, 'https://cards.scryfall.io/normal/front/9/f/9fae9044-a859-434d-8dc6-4f9d455ca5e1.jpg?1706242241'))
disguise_list.append(Disguise("Sanguine Savior", ['WB', 'WB'], 2, 2, 1, True, 'https://cards.scryfall.io/normal/front/9/c/9cba5503-ba99-43d8-8062-66d905e0d86b.jpg?1706242243'))

disguise_list.append(Disguise("Shady Informant", ['RB', 'RB'], 4, 4, 2, False, 'https://cards.scryfall.io/normal/front/0/d/0de36e63-8190-415f-b65b-bae1e595845d.jpg?1706242250'))
disguise_list.append(Disguise("Undercover Crocodelf", ['UG', 'UG'], 5, 5, 5, False, 'https://cards.scryfall.io/normal/front/5/b/5bc669c8-6f39-4d52-82d3-a4005d41c8a5.jpg?1706242271'))
disguise_list.append(Disguise("Lumbering Laundry", [], 5, 4, 5, False, 'https://cards.scryfall.io/normal/front/0/8/080ad039-1669-4735-9864-76f4c61fc59e.jpg?1706242318'))
disguise_list.append(Disguise("Branch of Vitu-Ghazi", [], 3, 0, 0, False, 'https://cards.scryfall.io/normal/front/7/3/73a8169f-b858-47a5-9c76-2e7c50ad4ecd.jpg?1706242330'))
