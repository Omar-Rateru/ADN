public class Multiplication extends Operation {
	
	public Multiplication (Expression ope1, Expression ope2) {
		super(ope1, ope2);
	}
	
	public int valeur() {
		return super.GetOperande1().valeur()*super.GetOperande2().valeur();
	}
	
	public String toString() {
		return "("+super.GetOperande1().valeur()+"x"+super.GetOperande2().valeur()+")";
	}	
	
}
