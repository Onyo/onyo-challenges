//
//  CategoryViewController.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit

class CategoryViewController: UIViewController {

    //MARK: - Properties
    
    @IBOutlet var collectionView: UICollectionView!
    
    var categories = [Category]()
    
    let collectionCellHeight = 190
    let cellPadding: CGFloat = 25.0
    
    // MARK: - Life Cycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        configContent()
    }
    
    // MARK: - Configuration
    
    func configContent() {
        let imageView = UIImageView(image:UIImage(named: "icon-bakedPotato"))
        parentViewController!.navigationItem.titleView = imageView
        parentViewController!.navigationItem.rightBarButtonItem = UIBarButtonItem(image: UIImage(named: "icon-onyo"), style: .Done, target: self, action: nil)
    }
    
}

extension CategoryViewController: UICollectionViewDataSource, UICollectionViewDelegate {
    
    func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return categories.count
    }
    
    func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCellWithReuseIdentifier(NibObjects.reuseIdentifierFor(.CategoryCollectionViewCell), forIndexPath: indexPath) as! CategoryCollectionViewCell
        cell.configureCellWith(categories[indexPath.row])
        
        return cell
    }
    
    func collectionView(collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView {
        if kind == UICollectionElementKindSectionHeader {
            let headerView = collectionView.dequeueReusableSupplementaryViewOfKind(kind, withReuseIdentifier: "CollectionHeaderView", forIndexPath: indexPath)
            return headerView
        } else {
            assert(false, "Unexpected element kind")
        }
    }
    
    func collectionView(collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAtIndexPath indexPath: NSIndexPath) -> CGSize {
        return CGSize(width: Int(view.bounds.width/2 - cellPadding), height: collectionCellHeight)
    }
}
