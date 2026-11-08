## ACTIVITY 5 Answer the following questions

1. What do all the methods (move(), special_move(), use()) in the previous activities have in
common?
    All the methods share the exact same method name across different classes. Even though each class prints a different message, they all have the required method name so the main function or loop can call them easily

2. How does this activity show polymorphism in a gaming context?

    This activity shows polymorphism because the main code can treat different game elements (like Warrior, Mage, and Archer) the exact same way. It can call perform_move() or apply_item() in a loop without checking their specific class type, as long as they all share the required method.

3. Can you think of other examples where the same action behaves differently depending on
the character or item?

    An example that i can think of is the attack() method that can be used on the Warrior, Mage, and Archer, and it can output different things depending on the class. For example, using attack() method on a Warrior can output a string that says "Swoosh! *Clank*" while the mage can output "Fzzz-pop!" and the archer outputs "Pew!".