import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();
    // Instance variables (if needed)

    public static void main(String[] args) {
    	Scanner scnr = new Scanner(System.in);
    	String menuChoice = "x";
    	
        initializeDogList();
        initializeMonkeyList();
        
        //Display menu and wait for choice. Warns if invalid choice made.
        while (!menuChoice.equals("q")) {
        	displayMenu();
        	menuChoice = scnr.nextLine();
        	
        	switch(menuChoice) {
        	case "1":
        		intakeNewDog(scnr);
        		break;
        	case "2":
        		intakeNewMonkey(scnr);
        		break;
        	case "3":
        		reserveAnimal(scnr);
        		break;
        	case "4":
        		printAnimals("dogs");
        		break;
        	case "5":
        		printAnimals("monkeys");
        		break;
        	case "6":
        		printAnimals("unreserved");
        	case "q":
        		break;
        	default:
        		System.out.println("Invalid option. Please choose from the menu.");
        		break;
        	}
        	
        }

    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");
        Dog dog4 = new Dog("Peepa", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", false, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
        dogList.add(dog4);
    }


    // Adds monkeys to a list for testing
    //Optional for testing
    public static void initializeMonkeyList() {
    	Monkey monkey1 = new Monkey("Mikey", "Capuchin", "36", "male", "4", "12", "14", "21", "01-01-2001", "United States", "in service", false, "United States");
    	Monkey monkey2 = new Monkey("Joey", "Macaque", "36", "male", "4", "12", "14", "21", "01-01-2001", "United States", "in service", false, "Canada");
    	Monkey monkey3 = new Monkey("Smokey", "Capuchin", "36", "male", "4", "12", "14", "21", "01-01-2001", "United States", "in service", true, "United States");
    	Monkey monkey4 = new Monkey("Butch", "Marmoset", "36", "male", "4", "12", "14", "21", "01-01-2001", "United States", "in service", false, "Mexico");
    	Monkey monkey5 = new Monkey("Clyde", "Capuchin", "36", "male", "4", "12", "14", "21", "01-01-2001", "United States", "in service", true, "United States");
    	
    	monkeyList.add(monkey1);
    	monkeyList.add(monkey2);
    	monkeyList.add(monkey3);
    	monkeyList.add(monkey4);
    	monkeyList.add(monkey5);
    }


    // Complete the intakeNewDog method
    // The input validation to check that the dog is not already in the list
    // is done for you
    public static void intakeNewDog(Scanner scanner) {
        System.out.println("What is the dog's name?");
        String name = scanner.nextLine();
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu
            }
        }

        // Get Dog information from user
        System.out.println("What is the dog's breed?");
        String breed = scanner.nextLine();
        System.out.println("Is the dog male or female?");
        String gender = scanner.nextLine();
        System.out.println("How old is the dog?");
        String age = scanner.nextLine();
        System.out.println("How much does the dog weight in pounds?");
        String weight = scanner.nextLine();
        System.out.println("Enter today's date (mm-dd-yyyy):");
        String today = scanner.nextLine();
        System.out.println("In what country was the dog acquired?");
        String country = scanner.nextLine();
        
        //Create new Dog object from input info and add to dogList
        Dog myDog = new Dog(name,breed,gender,age,weight,today,country,"intake",false,country);
        dogList.add(myDog);
    }


        // Complete intakeNewMonkey
    public static void intakeNewMonkey(Scanner scanner) {
    	
    	//Create arraylist of allowed species
    	ArrayList<String> monkeySpecies = new ArrayList<String>();
    	monkeySpecies.add("Capuchin");
    	monkeySpecies.add("Guenon");
    	monkeySpecies.add("Macaque");
    	monkeySpecies.add("Marmoset");
    	monkeySpecies.add("Squirrel Monkey");
    	monkeySpecies.add("Tamarin");
    	
    	
    	//Check if name exists already		
        System.out.println("What is the monkey's name?");
        String name = scanner.nextLine();
        for(Monkey monkey: monkeyList) {
            if(monkey.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis monkey is already in our system\n\n");
                return; //returns to menu
            }
        }

        // Get Monkey species from user and check if valid
        String species = "unknown";
        while (!monkeySpecies.contains(species)) {
        	System.out.println("What is the monkey's species? Must be one of:\nCapuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, Tamarin");
            species = scanner.nextLine();
        }
       
        //Get remaining information
        System.out.println("Is the monkey male or female?");
        String gender = scanner.nextLine();
        System.out.println("How tall is the monkey?");
        String height = scanner.nextLine();
        System.out.println("How long is the monkey's tail?");
        String tailLength = scanner.nextLine();
        System.out.println("How long is the monkey's body?");
        String bodyLength = scanner.nextLine();
        System.out.println("How old is the monkey?");
        String age = scanner.nextLine();
        System.out.println("How much does the monkey weigh in pounds?");
        String weight = scanner.nextLine();
        System.out.println("Enter today's date (mm-dd-yyyy):");
        String today = scanner.nextLine();
        System.out.println("In what country was the monkey acquired?");
        String country = scanner.nextLine();
        
        //Create new monkey object from input info and add to monkeyList
        Monkey myMonkey = new Monkey(name,species,height,gender,age,tailLength,bodyLength,weight,today,country,"intake",false,country);
        monkeyList.add(myMonkey);
    }
	
        // Complete reserveAnimal
        // You will need to find the animal by animal type and in service country
        public static void reserveAnimal(Scanner scanner) {
        	boolean madeReservation = false;
        	boolean validInput = false;
        	String animalType = "";
        	String serviceCountry;
        	
        	//Ask and validate animal type and location
        	while (!validInput) {
        		System.out.println("What type of animal do you want to reserve? [dog/monkey]");
        		animalType = scanner.nextLine();
        		if ((animalType.equalsIgnoreCase("dog")) || (animalType.equalsIgnoreCase("monkey"))){
        			validInput = true;
        			animalType = animalType.toLowerCase();
        		}
        	}
        	System.out.println("In which country do you need to reserve a service animal?");
        	serviceCountry = scanner.nextLine();
        	serviceCountry = serviceCountry.toLowerCase();
        	
        	switch(animalType) {
        	case "dog":
        		//Check for available dog in serviceCountry
        		for(Dog dog: dogList) {
                    if(!dog.getReserved() && dog.getInServiceLocation().equalsIgnoreCase(serviceCountry) && dog.getTrainingStatus().equalsIgnoreCase("in service")) {
                    	dog.setReserved(true);
                        System.out.println("\n\n" + dog.getName() + " has been reserved.\n\n");
                        madeReservation = true;
                        return; //returns to menu
                    }
                }
        	
        	case "monkey":
        		//Check for available monkey in serviceCountry
            	for(Monkey monkey: monkeyList) {
                    if(!monkey.getReserved() && monkey.getInServiceLocation().equalsIgnoreCase(serviceCountry) && monkey.getTrainingStatus().equalsIgnoreCase("in service")) {
                    	monkey.setReserved(true);
                    	System.out.println("\n\n" + monkey.getName() + " has been reserved.\n\n");
                        madeReservation = true;
                        return; //returns to menu
                    }
                }
        	
        	}//End of Switch/Case block
        	
        	//Inform user if no match found
        	if (!madeReservation) {
        		System.out.println("There are no animals that meet your criteria available.");
        	}
        	

        }

        // Complete printAnimals
        // Include the animal name, status, acquisition country and if the animal is reserved.
        // Remember that this method connects to three different menu items.
        // The printAnimals() method has three different outputs
        // based on the listType parameter
        // dog - prints the list of dogs
        // monkey - prints the list of monkeys
        // available - prints a combined list of all animals that are
        // fully trained ("in service") but not reserved 
        // Remember that you only have to fully implement ONE of these lists. 
        // The other lists can have a print statement saying "This option needs to be implemented".
        // To score "exemplary" you must correctly implement the "available" list.
        public static void printAnimals(String listType) {
        	//decide which list to print based on passed menu choice
        	switch(listType) {
        	case "dogs":
        		System.out.println("Dog list not yet implemented");
        		break;
        	case "monkeys":
        		System.out.println("Monkey list not yet implemented");
        		break;
        	case "unreserved":
        		//Scan both arrays and pick out animal that are unreserved
        		System.out.println("The following animals are fully trained and not reserved:\n");
        		
        		//Find unreserved dogs
        		for(Dog dog: dogList) {
                    if(dog.getTrainingStatus().equalsIgnoreCase("in service") && (!dog.getReserved())) {
                        System.out.println(dog.getName() + " (dog) is available in " + dog.getInServiceLocation());
                    }
                }
        		
        		//Find unreserved monkeys
        		for(Monkey monkey: monkeyList) {
                    if(monkey.getTrainingStatus().equalsIgnoreCase("in service") && (!monkey.getReserved())) {
                        System.out.println(monkey.getName() + " (monkey) is available in " + monkey.getInServiceLocation());
                    }
                }
        		
        		break;	
        	
        	}
        		
        }
}

