public class Division extends Operation {
	
	public Division (Expression ope1, Expression ope2) throws Exception{
		super(ope1, ope2);
		if (ope2.valeur() == 0) {throw new Exception("le diviseur est nul");}
	}
	
	public int valeur(){
		return super.GetOperande1().valeur()/super.GetOperande2().valeur();
	}
	
	public String toString() {
		return "("+super.GetOperande1().valeur()+"/"+super.GetOperande2().valeur()+")";
	}	
	
}
