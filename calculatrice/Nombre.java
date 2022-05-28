public class Nombre extends Expression {

	private int valeurNombre;
	
	public Nombre(int val) {
		this.valeurNombre = val;
	}
	
	public Nombre() {
		this.valeurNombre = 0;
	}
	
	public Nombre(Nombre nb) {
		this.valeurNombre = nb.valeur();
	}

	public int valeur() {return this.valeurNombre;}
}
