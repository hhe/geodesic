[V,E,F] = createIcosahedron();
V = 2*V./V(12,3) - repmat([0,0,1],12,1)


SUBDIV = 11
clf
allPoints=[]
figure(1)
hold on
for i=1:20
    points=[]
    p0 = V(F(i,1),:)
    p1 = V(F(i,2),:)
    p2 = V(F(i,3),:)
    % points = [points;(p0+p1+p2)/norm(p0+p1+p2)];

    for s=0:1:SUBDIV-1
        a0 = interpGreatCircle(p0,p1,s/SUBDIV);
        a1 = interpGreatCircle(p0,p2,s/SUBDIV);
        a1_ = interpGreatCircle(p2,p1,s/SUBDIV);
        a1__ = interpGreatCircle(p1,p0,s/SUBDIV);
        if s <= SUBDIV/2 && s > 0
            points = [points;a1];
            points = [points;a1_];
            points = [points;a1__];
        end
        for t=1:s-1
            b0 = interpGreatCircle(p0,p1,t/SUBDIV);
            b1 = interpGreatCircle(p2,p1,t/SUBDIV);

            c0 = interpGreatCircle(p1,p2,(s-t)/SUBDIV);
            c1 = interpGreatCircle(p0,p2,(s-t)/SUBDIV);

            options = optimset('TolFun',1e-8, 'TolX', 1e-8);
            p = fminsearch(@(x)costFunc(x, a0, a1, b0, b1, c0, c1),(a0+a1+b0+b1+c0+c1)./6,options);
            points = [points;p];
        end
    end
    row_idx = (points(:, end) > 0);
    points = points(row_idx, :)
    plot3(points(:,1),points(:,2),points(:,3), 'o')
    allPoints=[allPoints;points];
end
row_idx = (V(:, end) > 0);
V = V(row_idx, :)
plot3(V(:,1),V(:,2),V(:,3), 'o')
allPoints=[allPoints;V];
plot3(0, 0, -1, '.')

ssc = @(v) [0 -v(3) v(2); v(3) 0 -v(1); -v(2) v(1) 0]
RU = @(A,B) eye(3) + ssc(cross(A,B)) + ssc(cross(A,B))^2*(1-dot(A,B))/(norm(cross(A,B))^2)

allMatrices=[]
for i=1:size(allPoints,1)
    if allPoints(i,:) == [0 0 1]
        M = [1 0 0;0 1 0;0 0 1];
    else
        M=RU([0,0,1],allPoints(i,:));
    end
    M=[M (allPoints(i,:)*141)'];
    allMatrices=[allMatrices;reshape(M',[1 12])];
end
% M = 0.5.*[-394 0 0;0 0 388.5;0 390 0] % change according to different dome
M = [-1 0 0;0 0 1;0 1 0] % change according to different dome
allPoints3D=[]
for i=1:size(allPoints,1)
allPoints3D=[allPoints3D;allPoints(i,:)*M];
end
dlmwrite('606Holes_highp.csv', allPoints3D, 'precision', 8)
dlmwrite('mats.csv', allMatrices, 'precision', 7)