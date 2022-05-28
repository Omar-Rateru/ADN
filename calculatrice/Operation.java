public abstract class Operation extends Expression{
	private Expression operande1;
	private Expression operande2;
	
	public Operation (Expression ope1, Expression ope2) {
		this.operande1 = ope1;
		this.operande2 = ope2;
	
	}
	
	public Operation () {}
	
	public Operation(Operation o) {
		this.operande1 = o.GetOperande1();
		this.operande2 = o.GetOperande2();
	}
	
	public abstract int valeur();
	
	
	public Expression GetOperande1() {return this.operande1;}
	public Expression GetOperande2() {return this.operande2;}
}
