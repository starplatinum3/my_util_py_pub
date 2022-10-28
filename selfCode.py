def make_code(self):
    return f"""
            <mxCell id="{self.diagram_name}-level-{self.level}-line-{self.name}"
     style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
    edge="1" parent="1" source="{self.source}" target="{self.target}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>"""