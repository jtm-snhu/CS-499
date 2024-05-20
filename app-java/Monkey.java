
public class Monkey extends RescueAnimal{
	
	//Instance variables
	private String species;
	private String height;
	private String tailLength;
	private String bodyLength;
	
	
	//Constructor
	public Monkey (String name, String species, String height, String gender, String age,
	    String tailLength, String bodyLength, String weight, String acquisitionDate, String acquisitionCountry,
		String trainingStatus, boolean reserved, String inServiceCountry){
			setName(name);
	        setSpecies(species);
	        setHeight(height);
	        setGender(gender);
	        setAge(age);
	        setTailLength(tailLength);
	        setBodyLength(bodyLength);
	        setWeight(weight);
	        setAcquisitionDate(acquisitionDate);
	        setAcquisitionLocation(acquisitionCountry);
	        setTrainingStatus(trainingStatus);
	        setReserved(reserved);
	        setInServiceCountry(inServiceCountry);
		}
		
	//Monkey specific mutator methods
	public void setSpecies(String newSpecies) {
		species = newSpecies;
	}
	
	public void setHeight(String newHeight) {
		height = newHeight;
	}
	
	public void setTailLength(String newTailLength) {
		tailLength = newTailLength;
	}
	
	public void setBodyLength(String newBodyLength) {
		bodyLength = newBodyLength;
	}
	
	//Monkey specific access methods
	public String getSpecies() {
		return species;
	}
	
	public String getHeight() {
		return height;
	}
	
	public String getTailLength() {
		return tailLength;
	}
	
	public String getBodyLength() {
		return bodyLength;
	}

}