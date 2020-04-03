# vegetables = [vegetable_poha, millet_upma, mixed_vegetable_poriyal, bhindi_masala, mixed_vegetable_makhanwala]
# non_vegetables = [chicken_skewers, chicken_korma]
# other = [coconut_chutney, tamarind_chutney, tomato_chutney, lemon_pickle, lemon_rice, tomato_rice,
#             pakoda,aloo_tikki, bhel_puri]

from __future__ import print_function
import random

# --------------- Helpers that build all of the responses ----------------------

vegetable_poha = ["vegetable poha",
             """
             Ingredients required. 1 Cup red rice poha. <break time='1s'/>
             1 Cup grated vegetables or diced steamed vegetables. 
             1 tea spoon of mustard seeds. <break time='1s'/>
             green chillies for taste. 
             one fourth tea spoon turmeric.<break time='1s'/>
             salt. 
             2 table spoons of roasted peanuts. 
             2 table spoons of grated coconut.<break time='1s'/>
             2 table spoons of fresh coriander chopped
             """,
            """Put the poha in a big strainer and wash it. <break time='1s'/> Let it sit for about 5 minutes till the grains become thicker.
              Meanwhile, put a pan on low flame and add the mustard seeds.  <break time='1s'/>  Once they start popping, 
            add the green chillies, ginger and vegetables. <break time='1s'/>  Add salt and turmeric. 
            Sprinkle some water if it's too dry. <break time='1s'/>  After about three or four minutes add the soaked poha 
            and toss it around till it is fully coated with the turmeric. <break time='1s'/>  Add in the peanuts and take it off the stove. 
            Garnish with granted coconut and coriander"""
            ]

millet_upma = ["millet uppma",
            """
            1 cup barnyard millet.
            Half cup grated unpeeled carrot. <break time='1s'/>
            one fourth cup grated unpeeled beetroot.
            half cup finely grated coconut. <break time='1s'/>
            1 tea spoon of black mustard seeds.
            5 to 6 curry leaves. <break time='1s'/>
            one fourth cup roasted peanuts.
            salt, red chili powder to taste. <break time='1s'/>
            lemon juice to taste.
            """,
            """
            Wash the millets and soak them for 6 to 8 hours.<break time='1s'/>  Rinse with fresh water and
            cook in 1.5 to 2 times the quantity of water.  <break time='1s'/>
            Dry roast the mustard seeds and curry leaves in a wok.
            Once the millet has cooled down, mix it with the carrots, beetroot and coconut, salt, <break time='1s'/>
            chili powder and lemon juice. <break time='1s'/>
              Season with the dry roasted mustard and curry leaves. 
            Mix the peanuts in last to retain the crunch. <break time='1s'/>
              Serve with any green chutney on the side.
            """
            ]
            
mixed_vegetable_poriyal = [
    "mixed vegetable poriyal",
        """
        For the Vegetable  <break time='1s'/>
            half kg mixed unpeeled vegetables, finely chopped in cubes of 1 cm like beans,<break time='1s'/> carrots, potatoes and peas
            . 2 table spoons of grated fresh coconut.<break time='1s'/>
             
        For the Tempering  <break time='1s'/>
            1 tea spoon of mustard seeds. 
            ginger chili paste to taste. <break time='1s'/>
            1 red chili. 
            2-3 curry leaves. 
            salt to taste. <break time='1s'/>
            turmeric to taste. 
        """,
        """
        Steam the mixed vegetables <break time='1s'/>  so that they are just done but not overcooked  . 
        In a heated pan add mustard seeds. 
        When they spluter <break time='1s'/>  turn of the fame and add turmeric and dry roast. 
          When the smell permeates, add curry leaves and fnally mix in the steamed vegetables,
          ginger chili pasteand fresh coconut<break time='1s'/> . Serve hot.
        """
        ]
        
bhindi_masala = ["bhindi masala",
            """
            half kg bhindi washed, wiped and cubed. <break time='1s'/>
            Cut lengthwise 2 onions.
            cut lengthwise 2 tomatoes. <break time='1s'/>
            1 tea spoon of red chili.
            half tea spoon of amchur   means dry mango powder. <break time='1s'/>
            2 tea spoons of coriander powder and cumin powder.
            2 tea spoons of garam masala.  
            salt to taste. <break time='1s'/>
            turmeric to taste.
            coriander as garnish.
            """,
            
            """
            Mix all the dry masala and add to bhindi and steam. 
            The color should remain green.   <break time='1s'/>
             Amchur prevents the bhindi from becoming stcky.
            Saute the onion in a kadhai on high fame.   <break time='1s'/>
            When it browns, add tomato and saute for 30 seconds. 
              Add bhindi to this,and mix. <break time='1s'/>
            Garnish with coriander. If you want the bhindi crisp, afer steaming,<break time='1s'/>  bake in an oven for 5 minutes. 
              Serve.
            """
            ]
            
mixed_vegetable_makhanwala = [" mixed vegetable makhanwala",
            """
            6 to 8 large tomatoes steamed and pureed.<break time='1s'/>
            1 and half cups of mixed unpeeled vegetables   <break time='1s'/> cubed and steamed carrots, 
            potatoes, peas, caulifower and french beans.<break time='1s'/>
            1 green chili slit lengthwise.
            half tea spoon of cumin seeds.   <break time='1s'/>
            half tea spoon of garam masala. 
            half cup of cashew cream (made from one fourth of cup cashews and water).   <break time='1s'/>
            1 tea spoon of kasoori methi roasted and then powdered by hand
            3 table spoons of coriander <break time='1s'/>

            """,
            
            """
            Dry roast the cumin seeds. <break time='1s'/>
               First add the green chili and then add the 
            tomato puree and cook for a few minutes.  <break time='1s'/>  Keep 1 table spoon of cashew cream for garnish and
              add the rest to the tomato puree. 
            Cook for a few minutes   . <break time='1s'/>
            Add the vegetable garam masala and the kasoori methi powder. 
              Add 2 table spoons of coriander and mix. <break time='1s'/>
              Garnish with the remaining cream and coriander. 
              Serve hot.
            """
            ]
            
coconut_chutney = [
    "coconut chutney",
            """
            3 table spoons of coconut, shredded.
            1 inch fresh ginger, chopped. <break time='1s'/>
            1 fresh green chilli.  
            half bunch cilantro with stems and root removed. <break time='1s'/>
            fresh lemon juice. 
            salt to taste. <break time='1s'/>
            """,
            """
            In a food processor or blender add all ingredients into a pesto like sauce. 
            """
            ]

tamarind_chutney = [
    "tamarind chutney",
            """
            1 cup cleaned tamarind.
            half cup dates deseeded. <break time='1s'/>
            one fourth cup sugar. 
            2 cups water. <break time='1s'/>
            half tea spoon of red chilli powder.
            half crushed cumin seeds.
            1 tea spoon of salt. <break time='1s'/>
            three fourth cup jaggery 
            """,
            """
            Wash the tamarind clean. <break time='1s'/> Place the tamarind, jaggery, sugar, dates and water 
              in a deep boiling pan.
            Soak for a few minutes. <break time='1s'/>
              Put to boil for about 7-8 minutes. Cool to room temperature. 
              Blend in a electric blender till smooth.<break time='1s'/>  Strain and transfer to the pan again. 
              Boil till thick enough to coat the back of a spoon thinly.
              Add the seasoning. <break time='1s'/>
            Cool again. 
              Store in clean airtight bottles and refrigerate. 
            """
            ]
            
tomato_chutney = [
            "tomato chutney",
            """
            2 Table spoons of Ghee.
            one fourth tea spoon of red chillies. <break time='1s'/>
            1 tea spoon of cumin seeds.  
            1 inch ginger minced.
            1 inch of cinnamon stick. <break time='1s'/>
            2 cups coarsely fresh ripe tomatoes.  
            3 Table spoon of jaggery or brown sugar.
            Salt to taste. <break time='1s'/>
            """,
            """
            Heat ghee in a large sauce pan over moderate heat.  
            Add the cumin seeds and let sizzle and brown.  <break time='1s'/>
            Add red chillies, ginger and stir fry for a moment. 
             Add the other ingredients. Cook on low for about 20 to 35 minutes.  <break time='1s'/>
             Serve with meals. 
            """
            ]
            
lemon_pickle = [
    "lemon pickle",
        """
        6 Lemons.
        5 tea spoons of salt.
        5 tea spoons of chilli powder.  <break time='1s'/>
        Turmeric pinch.
        1 tea spoon of Hing. <break time='1s'/>
        1 tea spoon of methi.
        5 table spoons of oil. <break time='1s'/>
        """,
        """
        Cut lemons into small pieces and remove the seeds. Add salt and keep for about 12 hours. <break time='1s'/>
          Add chilli powder, turmeric, and methi. <break time='1s'/>
          Heat oil, mustard seeds, and asafoetida. Spread this mixture over the lemons. <break time='1s'/>
          Mix thoroughly. 
        """
            ]
            
lemon_rice = [
            "lemon rice",
            """
            1 cup of rice.
            2 table spoons of oil. <break time='1s'/>
            1 tea spoon of mustard seeds.  
            1 tea spoon of Urad Daal.
            1 tea spoon of Chana Daal. <break time='1s'/>
            handful of cashews.  
            handful of Raisins.
            Turmeric pinch.  <break time='1s'/>
            1 cup of mixed vegetables.
            2 Lemons. 
            """,
            """
            Cook rice. Heat oil and add all other ingredients except for the lemon. <break time='1s'/>
              Fry as appropriate.
              Mix stuff in pan with rice. Squeeze the lemon and add the juice to the rice. <break time='1s'/>
            """
            ]
            
tomato_rice = [
            "tomato rice",
            """
            1 cup of rice. 
            half can of tomatoes. <break time='1s'/>
            1 green pepper. 
            2 to 3 onions. <break time='1s'/>
            2 to 3 green chillies. 
            half inch of giner.  
            2 to 3 cloves of garlic. <break time='1s'/>
            fresh coriander bunch.
            some random spices
            """,
            """
            Fry cut onions, green pepper, ginger, garlic, random spices like <break time='1s'/>
              cloves, black pepper, cinnamon, cardamom, bay leaves and 
            salt for 5 - 10 minutes. <break time='1s'/>
              Add tomatoes, sauté for a while.
            Add washed and drained rice, fry for 5 minutes or so.  <break time='1s'/>
              Add more water and cook until rice is done. 
            """
            ]
            
pakoda = [
    "pakoda",
    """
        one and half cups of besan   means gram flour. <break time='1s'/>
        half tea spoon of red chilli powder. 
        Salt to taste. <break time='1s'/>
        1 cup of potatoes or onions  
        4 table spoons of minced cilantro. <break time='1s'/>
        one fourth cup of fresh fenugreek or methi leaves  
        oil for deep frying <break time='1s'/>
    """,
    """
        Mix the onions, cayenne pepper, salt and besan (also cilantro and methi). <break time='1s'/>
          Let it rest for about 10 minutes to allow the vegetables to sweat. <break time='1s'/>
          Add some water as much as required to make into a very thick paste. <break time='1s'/>
          Heat the oil for about 10 to 15 minutes on medium heat. <break time='1s'/>
          Pour a spoonful of the paste in the oil and let fry until golden brown. <break time='1s'/>
          Stir in between. Remove from oil and strain the oil out.
          Serve with tamarind chutney and mint chutney <break time='1s'/>
    """
            ]
            
aloo_tikki = [
            "aloo tikki",
            """
            6 oiled and peeled potatoes mashed fresh green chilli chopped finely for taste. <break time='1s'/>
            1 tea spoon of ginger (finely chopped).  <break time='1s'/>
            half cup of Cilantro leaves (chopped). <break time='1s'/>
            1 tea spoon of cayenne pepper. <break time='1s'/>
            1 table spoon of coriander powder.  <break time='1s'/>
            Salt to taste. <break time='1s'/>
            1 tea spoon of cumin powder. <break time='1s'/>
            1 tea spoon of mango powder called amchur.  
            Oil for pan frying. <break time='1s'/>
            """,
            """
            Boil the potato. Cool. Peel the skin and mash the potato. <break time='1s'/>
              Mix all ingredients except the oil.
              Make small hamburger size patties but about half inch high. <break time='1s'/>
              Pan Fry in a non-stick pan with oil until both sides are golden brown.
              Serve with tamarind or green chutney. 
            """
            ]
            
bhel_puri = [
            "bhel puri",
            """
            2 cups of puffed rice.
            1 cup of cooked chickpeas. <break time='1s'/>
            2 medium potatoes, cooked, peeled and cubed.  
            1 small onion, finely chopped.
            2 oz. crushed potato chips. <break time='1s'/>
            2 oz. salted peanuts.  
            1 table spoon of tomato sauce. <break time='1s'/>
            half tea spoon of salt or to taste.
            """,
            """
            Mix the puffed rice, chickpeas, potatoes, onions and peanuts. <break time='1s'/>
              Add tomato sauce, mix well and then sprinkle salt and the sev/potato chips. <break time='1s'/>
              The mixture must be made immediately before serving, <break time='1s'/>
              or the puffed rice will turn soggy.
            """
            ]
            
chicken_skewers = [
            "chicken skeweres",
            """
            4, boneless and skinless Chicken breast halves (about 1 pound).
            one third cup of Honey & Ginger Marinade.  <break time='1s'/>
            1, medium bell peppers (Such as yellow red or orange) cut into 1-inch pieces  
            8, wooden skewers. <break time='1s'/>
            Cooked white rice if desired.
            """,
            """
            Soak wooden skewers in cold water for at least 30 minutes. Rinse chicken, pat dry. <break time='1s'/>
              Cut chicken breasts lengthwise into 1-inch wide strips. <break time='1s'/>
              Place chicken in large, plastic food storage bag. <break time='1s'/>
              Add marinade. Let marinate in refrigerator for 2 hours.
              Meanwhile in boiling water, blanch peppers for 2 minutes. <break time='1s'/>
              Thread chicken onto skewers in an S-fashion, <break time='1s'/> leaving 1/4-inch spaces between pieces for even cooking.
              Add 2 pieces of bell pepper to each skewer. 
            Grill or broil until chicken is cooked through; 5-8 minutes. <break time='1s'/>
              For extra flavour, brush skewers with additional marinade. <break time='1s'/>
            If desired, serve with rice. 

            """
            ]
            
chicken_korma = [
            "chicken korma",
            """
            1 tablespoon vegetable oil.
            1 medium onion chopped. <break time='1s'/>
            1 pound boneless.  
            Skinless chicken breast diced. <break time='1s'/>
            half cup of broccoli florets.
            half cup sof liced carrots.  <break time='1s'/>
            1 Korma Cooking Sauce (15-ounce) jar. 
            three fourth cups of half-and-half 2 medium tomatoes   seeded and diced <break time='1s'/>
            """,
            """
            In large skillet, heat oil over medium-high heat. 
              Add onion and chicken. cook until chicken is cooked through, about 3-4 minutes. <break time='1s'/>
              Add the vegetables and cook for an additional 3 minutes. 
              Stir in Korma Cooking Sauce and simmer for 15 minutes or <break time='1s'/>
until the vegetables are cooked through.
              Stir in half-and-half and tomatoes.<break time='1s'/>
            Heat until warmed through. 
            """
            ]
cheela_tomato = [
            "cheela tomato",
            """
            1 pound tomatoes, peeled and pureed.
            1 pound besan or gram flour. <break time='1s'/>
            4 green chillies, minced.  
            1 small bunch of coriander leaves, minced. <break time='1s'/>
            1 teaspoon til (sesame seeds).
            1 teaspoon of turmeric powder. <break time='1s'/>
            Salt and chilli powder to taste.
            6 teaspoons of sugar .
            """,
            """
            Form a soft batter by mixing together all the above ingredients. <break time='1s'/>
            Heat a griddle (tawa) to smoking. Then lower the heat and grease it well with ghee.  <break time='1s'/>
            Put one fourth cup of batter on it and spread it into a thin even round shape.  <break time='1s'/>
            When the undersides turn golden, put a little more ghee around the edges and turn over.  
            Remove from heat when both sides turn golden brown. Serve piping hot with green chutney <break time='1s'/>
            """
            ]
            
salad_south=[
            "Salad in south indian style",
            """
            1 carrot, peeled and julienne.
            1 cucumber, peeled and diced. <break time='1s'/>
            1 tomato, diced.  
            1 green chilli (chilli pepper), minced. <break time='1s'/>
            1 small bunch of cilantro, coriander leaves minced.  
            salt and pepper to taste. <break time='1s'/>
            2 tablespoons lemon/lime juice.  
            For Salad Dressing.  
            2 teaspoons oil. <break time='1s'/>
            1 teaspoon brown mustard seeds.  
            1 teaspoon black gram dal (washed urad dal), picked over and rinsed.
            1 red chilli (chilli pepper), halved.  <break time='1s'/>
            half teaspoon asafoetida powder.
            A few curry leaves (optional) <break time='1s'/>
            """,
            """
            Add the first 7 ingredients in a bowl and mix thoroughly. And Keep aside.  <break time='1s'/>
            To make the salad dressing,  Heat 2 teaspoons oil in a heavy pan or skillet. <break time='1s'/>
              Add the mustard seeds, black gram dal, halved red chilli, asafoetida, and a few curry leaves. 
              When the mustard seeds splutter, add this mixture to the vegetables. <break time='1s'/>
              Now add the lemon juice, and mix thoroughly. Serve at room temperature.  <break time='1s'/>
            """
            ]
            
salad_north = [
            "salad in north indian style",
            """
            2 to 3 large Tomatoes, diced.
            2 large Cucumber, peeled and finely diced.  <break time='1s'/>
            one fourth cup Onion, finely diced.
            1 Green chilli, finely chopped. <break time='1s'/>
            A few sprigs of Coriander / Cilantro leaves.  
            1 to 2 teaspoons Sugar. <break time='1s'/>
            three fourth teaspoon Salt.  
            Lime juice to taste <break time='1s'/>
            hakf teaspoon of cumin seeds that are dry roasted in a skillet and then ground in a mortar 
            """,
            """
            Add all the ingredients in a bowl and mix thoroughly. <break time='1s'/>  Set aside.
            Serve at room temperature. 
            """
            ]
       
sprouted_md = [
            "sprouted Moong Dal",
            """
            2 cups sprouted green gram or moong dal.
            4 table spoons of onions finely chopped.  <break time='1s'/>
            2 cups of tomato and cucumber chopped.
            2 big lettuce leaves sliced fine.  <break time='1s'/>
            2 table spoons of roasted peanuts.
            A dash of lemon and salt to taste.  <break time='1s'/>
            """,
            """
            Gently mix all the ingredients except for the roasted peanuts in a salad bowl.  <break time='1s'/>
            Keep refrigerated.  <break time='1s'/>
            Mix in the roasted peanuts just before serving.  <break time='1s'/>
            Serve cold. 
            """
            ]
            
mango_ms = [
            "mango milk shake",
            """
            2 cups of mango pulp from a can or flesh of 3 ripen mangoes. 6 cups milk.  <break time='1s'/>
            3 Table spoons of sugar for canned mango pulp.  <break time='1s'/>
            More sugar if fresh mangoes used.  10 crushed ice cubes. <break time='1s'/>
            """,
            """
            Blend all the ingredients in a blender. <break time='1s'/>  Serve cold.
            The "mango nectar" that is widely available in grocery stores <break time='1s'/> does not have nearly enough mangoes per unit volume 
            to make this drink. 
            """
            ]
            
cold_coffee = [
            "cold coffee",
            """
            5 cups of old milk preferably whole.
            half cup of boiling water.  <break time='1s'/>
            6 tea spoons of instant coffee powder.
            3 table spoons of sugar crushed ice. <break time='1s'/>
            """,
            """
            Dissolve instant coffee powder and sugar in boiling water and allow to cool.  <break time='1s'/>
            Blend the coffee mixture and milk in a blender for few seconds.  <break time='1s'/>
            Add cream and crushed ice.  <break time='1s'/>
            Blend for another few seconds till it becomes frothy.  <break time='1s'/>
            Serve chilled.
            """
            ]

mango_lassi = [
            "mango lassi",
            """
            1 cup of plain yogurt. 
            1 cup of peeled and chopped ripe mango   or half cup of mango pulp. <break time='1s'/>
            sugar or to taste   if pulp is used then use less sugar.  
            one fourth tea spoon of cardamom powder (optional).  <break time='1s'/>
            Few ice-cubes. 
            """,
            """
            Combine all ingredients and blend until smooth in a blender. <break time='1s'/> Serve cold.
            """
            ]
            
nut_milk = [
            "nut milk",
            """
            2 glasses of whole milk.
            1 cup of water. <break time='1s'/>
            1 tablespoon of blanched almonds.  
            1 tablespoon of Pistachios. <break time='1s'/>
            1 tablespoon of Poppy Seeds.  
            6 cashew nuts. <break time='1s'/>
            Powdered cardamom, Cinnamon,   Nutmeg- a pinch each Honey as per taste <break time='1s'/>
            """,
            """
            Bring the water to boil in a small sauce pan. <break time='1s'/>  Add the spices.  
            Remove from heat and set aside to cool for 10 minutes.  <break time='1s'/>
            Make a fine paste of all the nuts and poppy seeds along with the heated spicesself. <break time='1s'/>
            Pour into a strainer lined with a damp cloth and set over a clean bowl.  <break time='1s'/>
            Squeeze all the milk out of the nuts by tightening the cloth by wringing it. <break time='1s'/>
            You may use the nut pulp   for thickening Indian curries or in baking.  <break time='1s'/>
            Mix this paste with the other spices into the milk and stir well. <break time='1s'/>  Mix the honey and chill. 
              Serve in glasses with crushed ice
            """
            ]
            
gulab_jamun = [
            "Gulab Jamun",
            """
            75 grams of Mawa.  
            A pinch of Sodium bi carbonate.  <break time='1s'/>
            75 grams of sugar.  
            two cardamoms.  <break time='1s'/>
            few drops of rose water.  
            10 grams of arrarot.  <break time='1s'/>
            40 ML of water. 
            """,
            """
            Prepare a sugar syrup of one string consistently with water.  <break time='1s'/>
            Sugar and rose water. Pass the Mawa through a strainer.  <break time='1s'/>
            Add crushed cardamom sieved arrarot and little cold water in which sodium bi-carbonate has been dissolved.  
            Make a soft clough without reading.  <break time='1s'/>
            Divide into equal portion and shape into small balls. <break time='1s'/>  Fry into a deep fat till brown.   
            Frying should be done on slow fire and it should be stirred constantly.  
              Remove, cool for a short while. <break time='1s'/>
            """
            ]
seviyan = [
            "Seviyan",
            """
            6 numbers of Dry dates.  
            1 tablespoon of Raisins. <break time='1s'/>
            1 tablespoon of Cashew nuts.  
            1 tablespoon of Sunflower seeds. <break time='1s'/>
            1 tablespoon of Blanched almonds.  
            1 tablespoon of Blanched pistachio. <break time='1s'/>
            three tablespoons of Ghee.  
            one fourth cup of Vermicelli. <break time='1s'/>
            4 cups of Milk.  
            2 teaspoons of Cardamom powder. <break time='1s'/>
            4 tablespoons of Sugar.
            """,
            """
            Soak the dates overnight. De-seed and chop into 4 pieces.  <break time='1s'/>
            Heat ghee and sauté the raisins, cashew nuts,   chironji seeds, almonds and pistachios for 2-3 minutes.  
            Drain and mix with the chopped dry dates.   Set aside. <break time='1s'/>
            In the same ghee, fry the vermicelli on a low flame for about 2 minutes,  
            stir continuously.  <break time='1s'/>
            Remove from heat and keep aside.  
            Boil the milk in a deep bottomed pan and add the vermicelli and sugar.   <break time='1s'/>
            Stir until the sugar dissolves.  
            Cook uncovered on a low flame for about 10 minutes  , stirr often.  <break time='1s'/>
            Add the fried dry fruits and cardamom powder, cover and cook for 3 minutes.  
            Serve hot or cold in individual bowls.  <break time='1s'/>
            """
            ]
            
kalakand = [
            "kalakand",
            """
            2 cups of full fat milk.
            1 cup of cottage cheese. <break time='1s'/>  
            half cup of sugar. 
            """,
            """
            Boil milk in a heavy bottomed saucepan until it reduces to half.   <break time='1s'/>
            Add cottage cheese and sugar and mix well till it attains a semi solid consistency.   
            Preheat the oven. <break time='1s'/>  Transfer the mixture to a square shaped oven proof dish and bake at 425F for 10 minutes. 
              Let stand in the oven for half and hour. <break time='1s'/>
              Cut into squares and serve. <break time='1s'/>
            """
            ]

vada = [
            "Vada",
            """
            half cup of Moong Daal.
            half cup of Urad Daal.  <break time='1s'/>
            one Onion.
            two tea spoons of Coriander.  <break time='1s'/>
            1 Green chilli.
            half tea spoon of Chilli powder.  <break time='1s'/>
            1 tea spoon of salt.
            1 tea spoon of Ginger.  
            half tea spoon of baking soda. <break time='1s'/>
            """,
            """
            Soak urad daal and moong daal for 2-3 hours.  <break time='1s'/>
            Grind daals into a coarse paste. <break time='1s'/>
            Add finely chopped onion, salt, coriander powder  <break time='1s'/> , chilli powder OR green chilli, ginger and soda. 
              Mix well and set aside for 4-5 minutes. <break time='1s'/>
              Fry small spoonfuls of the mixture in hot oil. 
            """
            ]

upma = [
            "upma",
            """
            2 table spoons of oil. 
            3 cups of water.  <break time='1s'/>
            1 onion. 
            2 cups of Ravva.  <break time='1s'/>
            1 cup of mixed vegetables.
            1 tea spoon of mustard seeds.  <break time='1s'/>
            1 tea spoon of Urad Daal.
            1 tea spoon of Chana Daal.  <break time='1s'/>
            1 tea spoon of Ginger.
            2 Green Chillies.  <break time='1s'/>
            1 Red Chilli.
            """,
            """
            Roast rava until light brown.  <break time='1s'/>
            Separately, fry mustard seeds, urad and chana daals, chopped onion, (crushed)  <break time='1s'/>
            red and (chopped) green chillies in oil. <break time='1s'/>
              Add water to the fried mixture, bring it to a boil,  lower the flame,
            and add the rava slowly,   stirring while doing so. <break time='1s'/>
              Optional: add cashews. <break time='1s'/>
            """
            ]
            
pani_puri = [
            "pani puri",
            """
            for pani puri stuffing -  <break time='1s'/>
            1 small to medium onion - optional.  <break time='1s'/>
            1 to 1.5 tablespoon chopped coriander leaves.  
            1 teaspoon of roasted cumin powder. <break time='1s'/>
            1 teaspoon of chaat masala powder.  
            one fourth teaspoon of red chili powder  <break time='1s'/>
            salt as required.  
            
            for pani recipe -  <break time='1s'/>
            half cup of tightly packed chopped mint leaves.
            1 cup tightly packed chopped coriander leaves. <break time='1s'/>
            1 inch ginger, chopped.  <break time='1s'/>
            2 to 3 green chilies, , chopped   (for a less spicy pani, add about 1 green chili). <break time='1s'/>
            1 tablespoon tightly packed tamarind. <break time='1s'/>
            3.5 to 4 tablespoons grated or powdered jaggery or sugar or add as required 
              or 1.5 tablespoons chopped seedless dates & 1.5 tablespoons powdered jaggery, <break time='1s'/>
              the sweetness can be adjusted as per your taste.
            1 teaspoon roasted cumin powder. <break time='1s'/>
            1 teaspoon chaat masala powder.  
            half cup water, for grinding.  <break time='1s'/>
            1 to 1.25 cups water to be added later, add water as per the consistency you want.  <break time='1s'/>
            1 to 1.5 tablespoons boondi (fried tiny gram flour balls), optional.  <break time='1s'/>
        
            """,
            """
            making pani puri stuffing  
            Boil the potatoes till they are cooked completely. <break time='1s'/>
            Peel them and then chop them.  
            Finely chop the onion if using it. <break time='1s'/>
            In a small bowl, mix the potatoes, onions, coriander leaves, cumin powder, <break time='1s'/>
            chaat masala powder and black salt or regular salt. <break time='1s'/>
            Mix well and keep aside. <break time='1s'/>
            making pani for pani puri  <break time='1s'/>
            In a blender add all the ingredients mentioned above for the pani.  
            Add water and grind to a fine chutney.  <break time='1s'/>
            Remove the green chutney in a large bowl.  
            Rinse the mixer jar with ½ cup water first and then add this water in the bowl.  <break time='1s'/>
            Then add three fourth cup more water.  <break time='1s'/>
            Mix well. Check the seasoning. Add more salt or jeera powder or chaat masala or jaggery if required. 
            If you want a thin pani, you could add some water. <break time='1s'/>  But keep on checking the seasoning, as per your taste.
            Add the boondi to the pani. <break time='1s'/>
            You can chill the pani in the fridge or add some ice cubes to it. <break time='1s'/>
            <break time='1s'/>
            making pani puri - <break time='1s'/>
            Crack the top of the puri with a spoon. <break time='1s'/>
            Add 2 to 3 teaspoons of the boiled potato-onion filling in the poori. <break time='1s'/>
            Stir the green pani first and then add it in the poori. <break time='1s'/>
            Optionally you can add some sweet chutney in the puri. <break time='1s'/>
            Serve the pani puri immediately. <break time='1s'/>

             You can also make individual portions with the puris, potato-onion mixture and the pani. <break time='1s'/>
             Let the individual assemble the pani puri for himself/herself as per his/her taste. <break time='1s'/>
            """
            ]

sambar = [
            "sambar",
            """
            1 table spoon of Tamcon. 
            1 table spoon of Mustard Seeds.  <break time='1s'/>
            Vegetables as needed.
            Turmeric pinch. <break time='1s'/>
            Salt to taste.  
            1 cup of Toor Daal. <break time='1s'/>
            2 to 3Curry Leaves.  
            2 tea spoons of Ghee. <break time='1s'/>
            """,
            """
            Boil toor daal and mash.  
            Boil tamcon in water until dissolved.  <break time='1s'/>
            Take the vegetables, slightly fry them, and add them to this tamarind water. <break time='1s'/>
            Add a little salt and turmeric and boil. <break time='1s'/>
            When vegetables are soft, add the toor daal paste and wait until the mixture boils again. <break time='1s'/>
            Lower the flame. <break time='1s'/>
            Add curry leaves, the Masala mixture, salt and boil for a few minutes, <break time='1s'/>
            stirr occasionally. <break time='1s'/>
            """
            ]
            
rasagolla = [
            "Rasagolla",
            """
            1 gallon of milk. <break time='1s'/>
            1 cup of lemon juice.
            1 cup of sugar. <break time='1s'/>
            """,
            """
            Bring one gallon of milk to a boil. <break time='1s'/>
            When boiling add one cup of either whiter vinegar or lemon juice.  <break time='1s'/>
            Turn the stove off. Milk should separate into whey and curd.  <break time='1s'/>
            Pour into colander, leaving only the panir/curd. Leave curd in strainer until cold and dry. <break time='1s'/>
            This will take at least an hour. Place curd in food processor and process for one minute.  <break time='1s'/>
            It should be soft but not sticky.  <break time='1s'/>
            Form small balls from the curd. Using vinegar usually results in about 80 to 100 rasagollas.  <break time='1s'/>
            Bring one cup sugar and 3 cups water to a boil in a pressure cooker.  <break time='1s'/>
            Place 20-25 rasagollas in syrup. Turn off the heat to place the cover on the pressure cooker.  
            Turn heat on high. When cooker begins to whistle wait for a couple of minutes, then turn it off.  <break time='1s'/>
            When pressure cooker depressurizes, remove cover and  <break time='1s'/> repeat previous step with the rest of the rasagollas.  
            Do not use the same sugar syrup more than once. <break time='1s'/>
            """
            ]
            
rasmalai = [
            "Ras Malai",
            """
            Ricotta Cheese.
            2 cups of Sugar.  <break time='1s'/>
            5 Cardamom pods.
            1 Bay leaf.  <break time='1s'/>
            1 tea spoon of Vanilla. 
            Rose Water To taste.  <break time='1s'/>
            """,
            """
            Mix 1.5 cups of sugar with the Ricotta cheese   <break time='1s'/>
            and bake it in a 400 degree Faranheit oven for about 1hr and 15 minutes <break time='1s'/>  in a flat dish covered with aluminium foil.
            The cheese should have hardened and turned a pale brown.  <break time='1s'/>
            Thicken the Half and Half by simmering over low heat for a long time.  <break time='1s'/>
            This is best done in a microwave. <break time='1s'/>
            if a microwave is not available, do it over low heat and stir frequently.  <break time='1s'/>
            Thicken until the volume drops to around half of the original volume.  <break time='1s'/>
            Add the remaining 0.5 cup sugar, cardamom pods, bay leaf, vanilla and rose water to the Half and Half. 
            Heat for a few minutes.  <break time='1s'/>
            After the cheese has been baked, cut it into 1 inch squares <break time='1s'/>  and add to the hot thickened half and half. 
              Cool for a few hours in the fridge. <break time='1s'/>
            """
            ]
            
cabbage_curry = [
            "cabbage curry",
            """
            2 table spoons of oil.
            1 tea spoon of Mustard seeds.  <break time='1s'/>
            1 tea spoon of Urad Daal.
            1 tea spoon of Cumin seeds. <break time='1s'/>
            1 Green Chilli.  
            1 cup of Mixed vegetables. <break time='1s'/>
            1 Cabbage medium size.
            Salt to taste.  
            Turmeric pinch. <break time='1s'/>
            """,
            """
            Heat oil, mustard seeds, Urad Daal, cumin seeds, <break time='1s'/> and green chilli. Roast for a few seconds.  
            Add mixed vegetables. and cabbage. Sprinkle salt and turmeric. <break time='1s'/>
            Cook on high heat for a couple of minutes, <break time='1s'/> then cover and cook on low until done.
            """
            ]
            
chocolate_cake = [
            "Chocolate Cake",
            """
            1 cup of unsweetened cocoa powder.
            2 and half cups of all-purpose flour. <break time='1s'/>
            2 cups of sugar.  
            1 and half teaspoons of baking powder. <break time='1s'/>
            1 teaspoon of baking soda.
            1 teaspoon of salt.  <break time='1s'/>
            3 large eggs.
            three fourth cup of vegetable oil. <break time='1s'/>
            half cup of sour cream.  
            2 teaspoons vanilla extract. <break time='1s'/>
            """,
            """
            Preheat the oven to 350 degrees F. <break time='1s'/>
            Coat two 9-inch-round cake pans with cooking spray and line the bottoms with parchment paper.  <break time='1s'/>
            Whisk the cocoa powder and  <break time='1s'/> 1 and half cups boiling water in a medium bowl until smooth; set aside. 
            Whisk the flour, sugar, baking powder, baking soda and salt in a large bowl until combined. <break time='1s'/>
            Add the eggs, vegetable oil, sour cream and vanilla and beat with a mixer on medium speed until smooth, about 1 minute.  
            Reduce the mixer speed to low; beat in the cocoa mixture in a steady stream until just combined, <break time='1s'/>
            then finish mixing with a rubber spatula. <break time='1s'/>
            Divide the batter between the prepared pans and tap the pans against the counter to help the batter settle.  <break time='1s'/>
            Bake until a toothpick inserted into the middle comes out clean, 30 to 40 minutes. <break time='1s'/>
            Transfer to racks and let cool 10 minutes,  <break time='1s'/>
            then run a knife around the edge of the pans and turn the cakes out onto the racks to cool completely.   <break time='1s'/>
            Remove the parchment. Trim the tops of the cakes with a long serrated knife to make them level, if desired. <break time='1s'/>
            """
            ]
            
bread_halwa = [
            "bread halwa",
            """
            5 Slices of Milk Bread.
            one third cup of Sugar. <break time='1s'/>
            1 cup of Milk.
            one fourth cup of Ghee. <break time='1s'/>
            5 Cashews.
            """,
            """
            Trim the edges of bread slices and cut into small squares,Set aside. <break time='1s'/>
            Add half of ghee in a pan and heat it.  <break time='1s'/> Add the bread pieces. 
            Keep roasting till it is golden brown. <break time='1s'/> Add milk first add 1/2 cup mash it well. 
            Then add another 1/2 cup. <break time='1s'/>
            Let it get cooked for a min. <break time='1s'/>  Then mash it well with the laddle. Now add sugar.  
            It will start to turn goey.  <break time='1s'/> At this stage slowly add ghee, little by little and keep mixing. 
            Reserve  a tsp of ghee alone. <break time='1s'/>
            Once it starts to leave the sides of the pan. <break time='1s'/>
            It is the right stage, now fry cashews in a tsp of ghee till golden and add it. <break time='1s'/>
            Give a quick mix and switch off. <break time='1s'/>
            Serve hot / warm.
            """
            ]
            
puri = [
            "Puri",
            """
            3 cups whole wheat flour.
            1 teaspoon melted ghee or oil. <break time='1s'/>
            salt as required.  
            water as required. <break time='1s'/>
            oil for deep frying.
            """,
            """
            Seive the whole wheat flour with salt. Add melted ghee or oil.  <break time='1s'/>
            Add little water at a time and knead well to form a dough. <break time='1s'/> The dough should not be soft but a little stiff and tight.  
            Divide the dough into small or medium pieces – about 12-14. <break time='1s'/>
            Make into medium sized or slightly small balls.  <break time='1s'/>
            Apply oil to dough ball. The idea of applying oil and not dusting with flour is so that while frying, <break time='1s'/>  the oil stays clean and you won’t see dark burnt flour particles inside the oil.
            Roll the dough evenly into circles which are neither too thin nor thick.  <break time='1s'/>
            Place the rolled poori in a plate and cover with a clean kitchen towel, <break time='1s'/>  so that they don’t dry up.
            Heat oil in a deep frying pan or kadai. <break time='1s'/>
            When the oil is sufficiently hot then add one poori at a time and fry gently pressing down with the frying spoon 
            or slotted spoon in a circular motion.  <break time='1s'/>
            Turn over when puffed up and fry till golden brown. <break time='1s'/>
            Serve poori hot with a vegetable curry. <break time='1s'/>
            """
            ]
            
            
mohan_thal = [
            "mohan thal",
            """
            115 grams of Besan.
            30 grams of Pistachio. <break time='1s'/>
            60 ml of Milk.  
            20 Cardmom. <break time='1s'/>
            sugar as required
            """,
            """
            Mix Gram flour with milk and 55gms fat.
            Make a thick sugar syrup. <break time='1s'/>
            Blanch and slice almonds and pistachio.  
            Add powdered cardamom. <break time='1s'/>
            Heat the remaining fat. Add besan and than fry.
            Add sugar syrup. Mix well. Remove and pour into a guessed tray and allow to set.  <break time='1s'/>
            Sprinkle cardamom powder.
            Garnish with nuts and cut into piece. <break time='1s'/>
            """
            ]
sweet_lassi = [
            "sweet lassi",
            """
            1 cup of Plain yogurt.
            2 table spoons of Sugar. <break time='1s'/>
            4 Ice Cubes.
            """,
            """
            Blend all the ingredients in an electric blender. <break time='1s'/> Serve cold. 
            """
            ]

panner_bm = [
            "Paneer Butter Masala",
            """
            Paneer - 200 gms cubed.
            1 Bay leaf. <break time='1s'/>
            1 tea spoon of Red chili powder.  
            one fourth cup of Milk or water. <break time='1s'/>
            Half tea spoon of Kasuri methi.
            one fourth tea spoon of Sugar.  <break time='1s'/>
            Salt to taste.
            2 table spoons of Butter or oil. <break time='1s'/>
            """,
            """
            Take all the ingredients mentioned under "For Gravy" in a mixer jar.
            Grind to a smooth paste using little water.  <break time='1s'/>
            In a pressure cooker, add the ground paste and the other main ingredients and mix well. <break time='1s'/>
            Place the cooker on the small burner of the stove and cook for 2 whistles over medium flame.  
            After the pressure gets released on its own, open the lid and mix well. <break time='1s'/>
            Transfer to the serving bowl and serve garnished with a dollop of cream on top and coriander leaves. <break time='1s'/>
            """
            ]
            
maggie = [
            "maggie",
            """
            Maggie packets.
            Oil as required. <break time='1s'/>
            onions, tomatoes, salt as required. <break time='1s'/>
            """,
            """
            First, heat the oil. Toss in the tomatoes, the onions and cook them well.  <break time='1s'/>
            Give them a little stirr and let them cook for a while.  <break time='1s'/>
            Take one packet of maggie and transfer it onto the dish. <break time='1s'/>
            Put the tomato onion mix right on top of the Maggie <break time='1s'/>  and you are done. 
            Serve the maggi after stirring it for a while. <break time='1s'/>
            """
            ]
            
panner_curry = [
            "panner curry",
            """
            200 grams of cubed paneer.
            1 big carrot. <break time='1s'/>
            onions, tomatoes, chillies and salt as required.  
            1 tea spoon of crushed ginger. <break time='1s'/>
            2 tea spoons of garam masala.  
            1 tea spoon of chilli powder and cumins seeds. <break time='1s'/>
            """,
            """
            Heat 1 tablespoon of butter or oil in a pan. Temper with cumin seeds.  <break time='1s'/>
            Add cubed onions and saute for a minute. <break time='1s'/>
            Add crushed ginger, slit green chillies and saute for a minute.  <break time='1s'/>
            Add chopped tomatoes and saute well, till the tomatoes shrink. <break time='1s'/>
            Add diced carrots and saute well in high flame for 3 to 5 minutes.  <break time='1s'/>
            Add salt, chilli powder and garam masala powder. <break time='1s'/>
            Add the paneer and saute for 2 minutes in medium flame.  <break time='1s'/>
            Now, You can serve paneer curry hot with roti or naan or rice
            """
            ]
            
Butter_chicken = [
            "Butter chicken",
            """
            3 chicken drumsticks or sliced breast pieces.
            1 table spoon of oil. <break time='1s'/>
            1 tea spoon of ginger paste. 
            1 tea spoon of garlic paste. <break time='1s'/>
            1 cup yogurt or buttermilk.
            1 cup sour cream. <break time='1s'/>
            half tomato puree.
            4 oz. butter. <break time='1s'/>
            6 cardamoms.  
            6 cloves. <break time='1s'/>
            2 sticks cinnamon.
            """,
            """
            Heat the oil in a large saucepan. <break time='1s'/>
            Fry the ginger, garlic, cardamoms, cinnamon <break time='1s'/>  and cloves on medium low heat for a minute, 
            and add the chicken with the yogurt or buttermilk, tomato puree, sour cream, <break time='1s'/>
            chilli powder and salt. <break time='1s'/>
            Cook on medium low heat, stirring occasionally , for half an hour,  <break time='1s'/>
            keeping the saucepan covered with a lid. <break time='1s'/>  Add butter before serving
            """
            ]

chicken_tikka = [
            "chicken tikka",
            """
            1 and half lbs. chicken breast; boneless and skinless. <break time='1s'/>
            1 teaspoon Chile powder.  <break time='1s'/>
            1 teaspoon coriander seeds, ground.
            2 tablespoons lime juiceself.  <break time='1s'/>
            2 garlic cloves.
            1 teaspoon grated fresh ginger.  <break time='1s'/>
            2/3 cup yogurt.
            """,
            """
            Rinse chicken, pat dry with paper towels and cut into three fourth inch cubes.  <break time='1s'/>
            Thread onto short skewers. Put skewered chicken into a shallow non metal dish.  <break time='1s'/>
            In a small bowl, mix together yogurt, ginger root, garlic,  <break time='1s'/>  chilli powder, coriander, salt, lime juice and oil. 
              Pour over skewered chicken and turn to coat completely in marinade. <break time='1s'/>
              Cover and refrigerate 6 hours or overnight to allow chicken to absorb flavours. <break time='1s'/>
              Heat grill. Place skewered chicken on grill rack and cook 5 to 7 minutes, <break time='1s'/>  turning skewers and
            basting occasionally with any remaining marinade. <break time='1s'/> Serve hot.
            """
            ]     
            
chicken_curry = [
            "chicken curry",
            """
            2 lb. chicken pieces.
            2 onions, chopped or pureed.  <break time='1s'/>
            2 tea spoons of ginger paste and garlic paste.
            1 tea spoon of turmeric powder, chilli powder, cumin powder.  <break time='1s'/>
            coriander leaves.
            tomatoes, salt as required <break time='1s'/>
            """,
            """
            Heat oil in a saucepan and fry the onions, ginger and garlic, <break time='1s'/>  together with coriander leaves,
            for five minutes on low heat . <break time='1s'/>
            Add tomato, chicken, turmeric and chilli powders   
            and salt together with half a cup of lukewarm water   <break time='1s'/>
            and cook on medium low heat for half an hour <break time='1s'/> , keeping the saucepan covered with a lid.
            """
            ]
            
tandoori_chicken=[
            "tandoori chicken",
            """
            10 chicken drumsticks.
            2 tablespoons plain yogurt. <break time='1s'/>
            2 tablespoons tomato paste.
            2 tablespoons fresh ginger, shredded.  
            6 cloves garlic, ground. <break time='1s'/>
            2 tablespoons lemon juice.  
            2 tablespoons vinegar.
            Red pepper, to taste.  <break time='1s'/>
            Garam Masala, to taste.
            2 tablespoons vegetable oil. <break time='1s'/>
            """,
            """
            Skin drumsticks and make cuts on the drumstick meat.  <break time='1s'/>
            Mix yogurt,   tomato paste,   ginger,  garlic, <break time='1s'/>
            lemon juice,  vinegar,  salt,  pepper and <break time='1s'/>
            Garam Masala. Marinate chicken in this paste for six hours. <break time='1s'/>
            Preheat oven to 350 degrees Farenheit and bake for 45 minutes. <break time='1s'/>
            """
            ]
            
fish_curry = [
            "fish curry",
            """
            Fish 500 grams.
            Green chillies 5 grams. <break time='1s'/>
            Onions 50 grams.  
            Tomatoes 55 grams. <break time='1s'/>
            Red Chillies 10 grams.
            Cumin seeds 20 grams.  <break time='1s'/>
            Tamarind 10 grams.
            Coriander 10 grams.  <break time='1s'/>
            Oil 30 ml.
            Coconut 115 grams <break time='1s'/>
            """,
            """
            Chop onions, Roast and grind red chillies, turmeric cumin seeds and coriander.  <break time='1s'/>
            Grind coconut to a fine paste. Combine all other spices.  <break time='1s'/>
            Fry onions in fat. Add grounded Masala and green chillies. Fry till flavour emerges. 
            Add chopped tomatoes and sufficient water soak tamarind in water and extract pulp.  <break time='1s'/>
            Cut fish into pieces.  <break time='1s'/>
            When the gravy boils, add fish.  <break time='1s'/>
            Add tamarind pulp, curry leaves and simmer till fish is cooked.  <break time='1s'/>
            """
            ]
            
fish_crisps = [
            "fish crisps",
            """
            10 Fish pieces.
            1 teaspoon Sunflower Oil , optional.  <break time='1s'/>
            5 teaspoon Red Chilli powder.
            2 teaspoon Turmeric powder. <break time='1s'/>
            salt and water as required.
            """,
            """
            In large vessel add red chilli powder <break time='1s'/> , turmeric powder, salt and water.  
            And make a fine paste and add the fish to it and mix well.  <break time='1s'/>
            Allow it to marinate for half an hour. <break time='1s'/>  Meanwhile line your baking tray with Parchment paper. 
            Preheat the oven at 180 Deg c for about 10 mins. <break time='1s'/>
            Arranged the marinated fish pieces in the lined baking tray and using grill mode grill it for 7 mins.<break time='1s'/> 
            After 7 mins flip the fish and then grill for another 7 mins. <break time='1s'/>
            Now that the colour of the fish would have slightly turned dark. <break time='1s'/>
            Flip the side of the fish once again and brush it with oil if required. <break time='1s'/>
            And grill for another 5 mins. <break time='1s'/>
            Once done flip the fish once again and brush with little oil <break time='1s'/>  and grill for another 5 mins.
            Fish would have cooked by now and it is ready to be served. <break time='1s'/>
            If you feel the fish is not yet cooked grill for another 4 mins <break time='1s'/>
            by flipping the fish sides after 2 mins. <break time='1s'/>
            Serve hot as an appetizer or starter. <break time='1s'/>
            """
            ]
            
chicken_pizza = [
            "chicken pizza",
            """
            1 thin pizza base (dinner plate size).  <break time='1s'/>
            2 tablespoons no-added-salt tomato paste.  <break time='1s'/>
            1 cup baby spinach leaves. <break time='1s'/>
            half large red onion, finely chopped. <break time='1s'/>
            100 grams of cooked or BBQ chicken breast, thinly sliced.  
            half small red capsicum, seeded and diced. <break time='1s'/>
            6 large cherry tomatoes halved.  
            half cup grated reduced-fat mozzarella cheese. <break time='1s'/>
            """,
            """
            pre heat oven to 220º celsius. <break time='1s'/>
            Spread tomato paste evenly over pizza base. <break time='1s'/>
            Top with spinach leaves, sliced onion, <break time='1s'/>  chicken, capsicum strips
            and cherry tomatoes. <break time='1s'/>
            Sprinkle with cheese   and place on a baking tray, pizza stone or wire rack.
            Bake for 5 minutes until cheese is melted <break time='1s'/>  then cover with foil to prevent burning. 
            Bake for a further 5 minutes until base is crisp. <break time='1s'/>
            Sprinkle with roughly torn basil leaves on top to serve. <break time='1s'/>
            """
            ]
            
egg_fry = [
            "egg fry",
            """
            1 to 3 eggs. <break time='1s'/>
            2 teaspoons of butter or oil.
            """,
            """
            Carefully break eggs into a small bowl.  <break time='1s'/>
            Heat oil in a large non-stick pan over medium heat.  <break time='1s'/>
            Once the pan is fully heated, carefully pour in the egg,  <break time='1s'/>
            and let it cook until the whites are completely set but the yolks are still soft.  
            Remove immediately and serve for sunny-side-up eggs.  <break time='1s'/>
            Remove and serve immediately, <break time='1s'/> seasoned with salt and pepper if you’d like.
            """
            ]
overall = [
    gulab_jamun, cold_coffee, mango_ms, mango_lassi, seviyan, 
    kalakand , nut_milk, coconut_chutney, tamarind_chutney, tomato_chutney, 
    lemon_pickle, maggie, sambar, pakoda, aloo_tikki,
    salad_south, salad_north, sprouted_md, bhel_puri, cheela_tomato,
    pani_puri, vada, upma, rasagolla, rasmalai,
    chocolate_cake, bread_halwa, puri, sweet_lassi, mohan_thal,
    
    panner_bm, vegetable_poha, panner_curry, tomato_rice, bhindi_masala,
    millet_upma, cabbage_curry, lemon_rice, mixed_vegetable_poriyal, mixed_vegetable_makhanwala,
    
    Butter_chicken, chicken_tikka, chicken_skewers, chicken_curry, chicken_korma,
    egg_fry, tandoori_chicken, fish_curry, fish_crisps, chicken_pizza
            ]
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak>"""+ output + "</speak>"

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_music1(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_sparkle_chimes_01"/>"""+ output + "</speak>"

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music2(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/home/amzn_sfx_food_frying_01"/>"""+ output + "</speak>"

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    

def build_speechlet_response_music5(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_02"/>"""+ output +
            """ <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_outro_01"/> </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music3(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/home/amzn_sfx_food_frying_01"/>"""+ output + 
            """ <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_waiting_loop_30s_01"/> </speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music4(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/musical/amzn_sfx_musical_drone_intro_02"/>"""+ output +
            """ </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    
    speech_output = """
    Hey! Welcome to the cooking store. Let's drive into the delicious world. 
    Get started by saying, Lets start cooking. 
      Say help me for further instructions"""
    
    reprompt_text = "I don't know if you heard me. Weclome to the cooking store. Say, let's get started."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music1(
        card_title, speech_output, reprompt_text, should_end_session))



def show_menu(intent, session):
    session_attributes = {}
    card_title = "Menu Card"
    temp = """
    Ok. Here is the menu of our cooking store.  
    <break time='1s'/> Select one of the following from below four.  . 
    Veg recepies. <break time='1s'/>  Non veg recepies.  
    Other recepies <break time='1s'/> such as chutneys and snacks.  
    and All recipies.  
    """
    speech_output = temp
    reprompt_text = "say all recepies to check our complete menu"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def all_menu(intent, session):
    session_attributes = {}
    card_title = "Menu Card"
    temp = "Ok. Here is the menu of all recipies of our cooking store. <break time='1s'/> Select a number associated with a recepie you wanna cook. "
    count = 1
    for o in overall:
        temp += ". " + str(count) +" "+ o[0] + "<break time='1s'/>"
        count += 1
    speech_output = temp
    reprompt_text = "Say   all recepies   to know again about all recepies."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
    
def veg_menu(intent, session):
    session_attributes = {}
    card_title = "Menu Card"
    temp = "Ok. Here is our veg menu of our cooking store.  <break time='1s'/> Select a number associated with a recepie you wanna cook. "
    count = 31
    for o in overall[30:40]:
        temp += ". " +str(count) +" "+ o[0] + "<break time='1s'/>"
        count += 1
        
    speech_output = temp
    reprompt_text = "Say <break time='1s'/>   veg recepies <break time='1s'/>  to know again about veg recepies."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
        
def nonveg_menu(intent, session):
    session_attributes = {}
    card_title = "Menu Card"
    temp = """
    Ok. Here is our non veg menu of our cooking store.   
    Select a number associated with a recepie you wanna cook. """
    count = 41
    for o in overall[40:]:
        temp += ". " + str(count) +" "+ o[0] + "<break time='1s'/>"
        count += 1
    speech_output = temp
    reprompt_text = "Say <break time='1s'/>  non veg recepies <break time='1s'/>  to know again about non veg recepies."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
        
def other_menu(intent, session):
    session_attributes = {}
    card_title = "Menu Card"
    temp = "Ok. Here is the other recepies menu of our cooking store. <break time='1s'/>  Select a number associated with a recepie you wanna cook. "
    count = 1
    for o in overall[:30]:
        temp += ". " + str(count) +" "+ o[0] + "<break time='1s'/>"
        count += 1
    speech_output = temp
    reprompt_text = "Say   other recepies   to know again about other recepies."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))

def choosing(intent, session):
    card_title = "Selected Recipie"
    choice = intent['slots']['number']['value']
    item = overall[int(choice) - 1][0]
    session_attributes = {'choice':choice}
    speech_output = "Ok. Let's start cooking " + item + """ 
    . <break time='1s'/> You can ask me about Ingredients and Process whenever you want and as many times as you want.  
    . Just Say Ingredients <break time='1s'/>  to know about ingredients being used. And Say Tutorial <break time='1s'/>  to get started with cooking.
    """
    reprompt_text = "Say Ingredients   for ingredients."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music2(
        card_title, speech_output, reprompt_text, should_end_session))



def tell_ingredients(intent, session):
    card_title = "Ingredients"
    choice = session['attributes']['choice']
    session_attributes = {'choice':choice}
    if session.get('attributes', {}):
        item = session['attributes']['choice']
        speech_output = overall[int(choice) - 1][1] +  """
          say Ingredients <break time='1s'/>  to repeat once again. Or Say Tutorial  <break time='1s'/> to get started with cooking.
        """
    reprompt_text = "Say Ingredients   to listen to the ingredients again."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music3(
        card_title, speech_output, reprompt_text, should_end_session))



def start_tutorial(intent, session):
    card_title = "Tutorial"
    choice = session['attributes']['choice']
    session_attributes = {'choice':choice}
    if session.get('attributes', {}):
        item = session['attributes']['choice']
        speech_output = overall[int(choice) - 1][2] + """
          say Tutorial <break time='1s'/>  to repeat once again. 
        Or Say Ingredients <break time='1s'/>  to know again about ingredients.
        """
    reprompt_text = "Say Tutorial   to listen to the Tutorial again."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music3(
        card_title, speech_output, reprompt_text, should_end_session))
        

def all_commands():
    card_title = "Help"
    session_attributes = {}
    speech_output = """"
    Here are some of the commands to use cooking store.  <break time='1s'/>
    Say let's start cooking to start.  <break time='1s'/>
    Say all recepies to see menu.  <break time='1s'/>
    Or directly, say the number of the recepie <break time='1s'/> you want to start cooking.  
    """
    reprompt_text = "Say Help   to listen to the commands again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
    
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Cooking store. " \
                    "Have a nice day!   Visit again"
    should_end_session = True
    return build_response({}, build_speechlet_response_music5(
        card_title, speech_output, None, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "StartCookingIntent":
        return show_menu(intent, session)
    elif intent_name == "SelectRecipieIntent":
        return choosing(intent, session)
    elif intent_name == "IngredientIntent":
        return tell_ingredients(intent, session)
    elif intent_name == "TutorialIntent":
        return start_tutorial(intent, session)
    elif intent_name == "VegIntent":
        return veg_menu(intent, session)
    elif intent_name == "NonVegIntent":
        return nonveg_menu(intent, session)
    elif intent_name == "OtherIntent":
        return other_menu(intent, session)
    elif intent_name == "AllIntent":
        return all_menu(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return all_commands()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if ('session' in event):
        print("event.session.application.applicationId=" +
              event['session']['application']['applicationId'])
        if event['session']['new']:
            on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
                           
    if ('request' in event):                       
        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])