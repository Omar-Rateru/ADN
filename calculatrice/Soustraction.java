public class Soustraction extends Operation {
	
	public Soustraction (Expression ope1, Expression ope2) {
		super(ope1, ope2);
	}
	
	public int valeur() {
		return super.GetOperande1().valeur()-super.GetOperande2().valeur();
	}
	
	public String toString() {
		return "("+super.GetOperande1().valeur()+"-"+super.GetOperande2().valeur()+")";
	}	
	
}
